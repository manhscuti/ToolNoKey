import requests
import base64
import os

def get_headers(token):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }

def validate_token():
    while True:
        token = input("🔑 Nhập GitHub Personal Access Token (PAT): ").strip()
        resp = requests.get("https://api.github.com/user", headers=get_headers(token))
        if resp.status_code == 200:
            username = resp.json()["login"]
            print(f"✅ Xác thực thành công. Tài khoản: {username}")
            return token, username
        else:
            print("❌ Token không hợp lệ. Vui lòng thử lại.")

def create_repo(token, repo_name):
    url = "https://api.github.com/user/repos"
    data = {
        "name": repo_name,
        "description": "Repo được tạo tự động",
        "private": False
    }
    response = requests.post(url, headers=get_headers(token), json=data)
    if response.status_code == 201:
        print(f"✅ Tạo repo '{repo_name}' thành công.")
    else:
        print("❌ Lỗi khi tạo repo:", response.json())
        exit()

def upload_file(token, username, repo_name, file_path, dest_path):
    url = f"https://api.github.com/repos/{username}/{repo_name}/contents/{dest_path}"
    with open(file_path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf-8")
    data = {
        "message": f"Add or update {dest_path}",
        "content": content
    }

    # Kiểm tra nếu file đã tồn tại -> cần SHA để update
    resp = requests.get(url, headers=get_headers(token))
    if resp.status_code == 200:
        sha = resp.json()["sha"]
        data["sha"] = sha

    response = requests.put(url, headers=get_headers(token), json=data)
    if response.status_code in [200, 201]:
        print(f"✅ Đã upload/chỉnh sửa file '{dest_path}' thành công.")
    else:
        print("❌ Lỗi khi upload file:", response.json())
        exit()

def delete_file(token, username, repo_name, file_path):
    url = f"https://api.github.com/repos/{username}/{repo_name}/contents/{file_path}"
    resp = requests.get(url, headers=get_headers(token))
    if resp.status_code != 200:
        print("❌ Không tìm thấy file hoặc lỗi khi lấy SHA:", resp.json())
        return

    sha = resp.json()["sha"]
    data = {
        "message": f"Delete {file_path}",
        "sha": sha
    }

    delete_resp = requests.delete(url, headers=get_headers(token), json=data)
    if delete_resp.status_code == 200:
        print(f"🗑️ Đã xoá file '{file_path}' thành công.")
    else:
        print("❌ Lỗi khi xoá file:", delete_resp.json())

def list_files(token, username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/contents/"
    response = requests.get(url, headers=get_headers(token))
    if response.status_code == 200:
        files = response.json()
        print("\n📂 Danh sách file trong repo:")
        for i, f in enumerate(files):
            print(f"{i + 1}. {f['name']}")
        return [f['name'] for f in files if f['type'] == 'file']
    else:
        print("❌ Không thể lấy danh sách file:", response.json())
        return []

def edit_file(token, username, repo_name):
    files = list_files(token, username, repo_name)
    if not files:
        print("❌ Không có file để chỉnh sửa.")
        return
    choice = input("🔢 Nhập số thứ tự file muốn chỉnh sửa: ").strip()
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(files):
        print("❌ Lựa chọn không hợp lệ.")
        return
    file_to_edit = files[int(choice) - 1]
    url = f"https://api.github.com/repos/{username}/{repo_name}/contents/{file_to_edit}"

    resp = requests.get(url, headers=get_headers(token))
    if resp.status_code != 200:
        print("❌ Lỗi khi lấy nội dung file:", resp.json())
        return

    content = base64.b64decode(resp.json()["content"]).decode("utf-8")
    print(f"\n📄 Nội dung hiện tại của '{file_to_edit}':\n{content}")
    new_content = input("\n📝 Nhập nội dung mới để thay thế toàn bộ: ")

    with open("temp_edit.txt", "w", encoding="utf-8") as f:
        f.write(new_content)

    upload_file(token, username, repo_name, "temp_edit.txt", file_to_edit)
    os.remove("temp_edit.txt")

def get_raw_url(username, repo_name, file_path):
    return f"https://raw.githubusercontent.com/{username}/{repo_name}/main/{file_path}"

def list_repos(token):
    url = "https://api.github.com/user/repos"
    response = requests.get(url, headers=get_headers(token))
    if response.status_code == 200:
        repos = response.json()
        print("\n📄 Danh sách repository hiện có:")
        for i, repo in enumerate(repos):
            print(f"{i + 1}. {repo['name']}")
        return [repo['name'] for repo in repos]
    else:
        print("❌ Không thể lấy danh sách repo.")
        exit()

def main():
    print("=== Tool Upload/Xoá/Chỉnh sửa File trên GitHub ===")

    token, username = validate_token()

    use_existing = input("📁 Bạn có muốn sử dụng repo hiện có không? (y/n): ").strip().lower()
    if use_existing == "y":
        repos = list_repos(token)
        if not repos:
            print("❌ Không có repo nào.")
            return
        choice = input("🔢 Nhập số thứ tự của repo muốn sử dụng: ").strip()
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(repos):
            print("❌ Lựa chọn không hợp lệ.")
            return
        repo_name = repos[int(choice) - 1]
        print(f"📦 Sử dụng repo: {repo_name}")
    else:
        repo_name = input("📦 Nhập tên repo muốn tạo: ").strip()
        create_repo(token, repo_name)
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(f"# {repo_name}\nRepo được tạo tự động.")
        upload_file(token, username, repo_name, "README.md", "README.md")

    while True:
        print("\n📌 Bạn muốn làm gì?")
        print("1. Upload file có sẵn")
        print("2. Tạo file mới")
        print("3. Xoá file khỏi repo")
        print("4. Chỉnh sửa file")
        print("5. Thoát")
        action = input("🔢 Chọn (1/2/3/4/5): ").strip()

        if action == "1":
            file_path = input("📂 Nhập đường dẫn file muốn upload: ").strip()
            if not os.path.exists(file_path):
                print("❌ File không tồn tại.")
                continue
            dest_name = os.path.basename(file_path)
            upload_file(token, username, repo_name, file_path, dest_name)
            print("🔗 Link RAW của file:", get_raw_url(username, repo_name, dest_name))

        elif action == "2":
            filename = input("📝 Nhập tên file muốn tạo (VD: code.txt): ").strip()
            content = input("💬 Nhập nội dung file: ")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            upload_file(token, username, repo_name, filename, filename)
            print("🔗 Link RAW của file:", get_raw_url(username, repo_name, filename))
            os.remove(filename)

        elif action == "3":
            files = list_files(token, username, repo_name)
            if not files:
                print("❌ Repo không có file nào để xoá.")
                continue
            choice = input("🔢 Nhập số thứ tự file muốn xoá: ").strip()
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(files):
                print("❌ Lựa chọn không hợp lệ.")
                continue
            file_to_delete = files[int(choice) - 1]
            delete_file(token, username, repo_name, file_to_delete)

        elif action == "4":
            edit_file(token, username, repo_name)

        elif action == "5":
            print("👋 Thoát chương trình. Tạm biệt!")
            break

        else:
            print("❌ Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
