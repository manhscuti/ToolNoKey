#==≠==≠==≠==≠==≠====≠==≠==≠==≠==≠==≠==#
#Copyright by JunidoKai
#Version : 2.2.4
#Python 3.12 
#17/07/2025 | 19:00:568
#Nếu decode vui lòng để lại comment này
#==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==≠==#
#==≠==Thư Viện==≠==#
import requests, base64, os, sys, socket
from time import sleep
#==≠==≠=Màu=≠==≠==#
xam = "\033[1;38;5;8m"
xla = "\033[1;38;5;10m"
vang = "\033[1;38;5;11m"
xduong = "\033[1;38;5;14m"
trang = "\033[1;38;5;15m"
xdam = "\033[1;38;5;21m"
xlv1 = "\033[1;38;5;42m"
xv1 = "\033[1;38;5;44m"
xlv2 = "\033[1;38;5;49m"
dv1 = "\033[1;38;5;50m"
la = "\033[1;38;5;79m"
vchuoi = "\033[1;38;5;154m"
do = "\033[1;38;5;196m"
mv1 = "\033[1;38;5;199m"
tim = "\033[1;38;5;201m"
cam = "\033[1;38;5;202m"
hdam = "\033[1;38;5;204m"
hong = "\033[1;38;5;211m"
vlightc = "\033[1;38;5;214m"
clightv = "\033[1;38;5;220m"
#==≠==≠=Thông Báo=≠==≠==#
done = xla + "[" + xlv2 + "✔" + xla +"]"
kt = xla + "[⊀" + trang + "/" + xla + "⊁]"  + trang + "=" + xv1 + ">"
error = vlightc + "[" + clightv + "!" + vlightc + "]"
#==≠==≠=Admin=≠==≠==#
wnn = xdam+"W"+xla+"h"+vang+"i"+do+"t"+cam+"e"+vchuoi+" NN"+xam
ma = hdam+"M"+hong+"i"+hdam+"n"+hong+"h"+hdam+"A"+hong+"n"+hdam+"h"+hong+"s🐰"+xam
jndk = xdam+"J"+xv1+"u"+xduong+"n"+xlv2+"i"+xlv1+"d"+xla+"o" +clightv+" K"+vlightc+ "a"+cam+"i"+xam
ht = wnn+trang+" & "+ma+trang+" & "+ jndk
#==≠==≠=IP=≠==≠==#
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
#==≠==Banner==≠==#
def minhanhs():
 os.system("cls" if os.name == "nt" else "clear")
 macuti = f"""               {ht}\n
⠀⠀⠀⠀⠀⣠⣶⣦⠀⠀⠀⣀⣤⣴⣶⣶ ⠀⠀⠀⠀⣀⣴⣦⠀     {dv1}Copyright{trang} : {ma}
⠀⠀⠀ ⣾⣿⣿⣿⣠⣴⣿⣿⣿⣿⣿⣿⠀⣀⣤⣶⣿⣿⣿⡟⠀     {dv1}Admin{trang}     : {wnn}
⣀⣀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀     {dv1}Admin{trang}     : {jndk}
⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣤⣤⣤
⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿     {xla}Name Tool{trang} :{xam}
⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁        {xlv2}         Banner{xam}
⠀⠀⣿⣿⡟⠀⠀⠀⠀{xla} ⡴⠖⠦{xam}⠼⢿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀
⠀⠀⣿⣿⠀⠀⠀⠀⠀{xla}⣼⣇⣋⡗{xam}⠀⠀⢿⣿⢻⣿⡟⢿⣿⣿⣷⠀     {dv1}Github   {trang} : {do}@404ERROR{xam}
⠀⣀⣿⣿⣤⣤⣤⣤⣤⣬⣭⣥⣤⣤⣤⣤⣤⣼⣿⣇⡀⠙⣿⡿⠀                 {do}@404ERROR{xam}
⠀⣿⣿⣿⠛⠻⣿⡟⠛⠛⠛⠛⠛⠛⣿⡿⠛⠻⣿⣿⡇⠀⠀⠀⠀                 {do}@404ERROR{xam}
⠀⣿⣿⣿⠀⠀⠀⣠⣾⣿⣿⣿⣿⣦⣀⠀{do}⣿{xam}⠀⣿⣿⡇⠀⠀⠀⠀
⠀⠙⢿⣿⣶⣾⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣶⣾⣿⠟⠁⠀⠀⠀⠀     {xduong}IP của bạn : {xlv2}{ip}{xam}
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣦⣴⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{do}                         Hoàng Xa - Trường Xa{trang} là của {vang}Việt Nam 🇻🇳

"""
 for X in macuti:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00010)
minhanhs()
#==≠==Soucre==≠==#
def ma_git():
    token = input(f"{xduong}Nhập Token {trang}: ").strip()
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }
    minhanhs()
    user = requests.get("https://api.github.com/user", headers=headers).json()
    print(" ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"  {xduong}{kt}   Tài khoản {trang}╗\n                      ╚≻ {mv1}{user['login']} {done}")
    print(" ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    return headers, user['login']

def ma_repo(headers, username):
    repos = requests.get(f"https://api.github.com/user/repos", headers=headers).json()
    if not repos:
        print("Bạn chưa có repo nào.")
    else:
        sleep(1)
        minhanhs()
        print(f"\n{kt} Repo hiện có :")
        for idx, repo in enumerate(repos):
            print(f"  {kt}{xla} Repo {idx+1}{trang}: {vang}{repo['name']}")
    choice = input("\nNhập số để chọn repo, hoặc gõ 'y' để tạo repo mới: ").strip()
    minhanhs()

    if choice.lower() == 'y' or not repos:
        repo_name = input("Nhập tên repo mới: ").strip()
        data = {
            "name": repo_name,
            "auto_init": True,
            "private": False
        }
        r = requests.post("https://api.github.com/user/repos", headers=headers, json=data)
        if r.status_code == 201:
            print(f"Repo '{repo_name}' đã được tạo.")
            return repo_name
        else:
            print(f"{error}Không tạo được repo.\n   Kiểm tra lại token hoặc quyền.")
            exit()
    else:
        try:
            repo_name = repos[int(choice)-1]['name']
            return repo_name
        except:
            print("Lựa chọn không hợp lệ. Thoát.")
            exit()

def ma_up_file(headers, username, repo):
    file_choice = input("\nChọn [1] Tải file từ máy lên\nChọn [2] Tạo file mới\nNhập lựa chọn: ").strip()
    if file_choice == '1':
        file_path = input("Nhập đường dẫn file: ").strip()
        file_name = os.path.basename(file_path)
        with open(file_path, "rb") as f:
            content = base64.b64encode(f.read()).decode()
    else:
        file_name = input("Nhập tên file mới (ví dụ: hello.txt): ").strip()
        text = input("Nhập nội dung file: ").strip()
        content = base64.b64encode(text.encode()).decode()
    #Tạo README.md nếu chưa có
    readme_url = f"https://api.github.com/repos/{username}/{repo}/contents/README.md"
    r = requests.get(readme_url, headers=headers)
    if r.status_code == 404:
        print("Tạo README.md...")
        data = {
            "message": "Add README.md",
            "content": base64.b64encode("# README".encode()).decode()
        }
        requests.put(readme_url, headers=headers, json=data)

    # Upload file
    file_url = f"https://api.github.com/repos/{username}/{repo}/contents/{file_name}"
    data = {
        "message": f"Add {file_name}",
        "content": content
    }
    r = requests.put(file_url, headers=headers, json=data)
    if r.status_code in [200, 201]:
        print(f"Đã upload file {file_name} thành công.")
        raw_link = f"https://raw.githubusercontent.com/{username}/{repo}/main/{file_name}"
        print(f"Link raw: {raw_link}")
    else:
        print("Lỗi upload file:", r.json())

def delete_file(headers, username, repo):
    url = f"https://api.github.com/repos/{username}/{repo}/contents/"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        items = [item for item in r.json() if item['type'] == 'file']
        if not items:
            print("Repo không có file nào để xoá.")
            return
        minhanhs()
        print(f"\n  {kt}Danh sách file:")
        for idx, item in enumerate(items):
            print(f"   {kt}{xla}File {idx+1}{trang}:{vang} {item['name']}")

        choice = input(f"Nhập số thứ tự file muốn xoá: ").strip()
        try:
            idx = int(choice) - 1
            file_info = items[idx]
            file_name = file_info['name']
            sha = file_info['sha']

            confirm = input(f"Bạn có chắc muốn xoá file [{file_name}] (y/n): ").strip().lower()
            if confirm == 'y':
                file_url = f"https://api.github.com/repos/{username}/{repo}/contents/{file_name}"
                data = {
                    "message": f"Delete {file_name}",
                    "sha": sha
                }
                r = requests.delete(file_url, headers=headers, json=data)
                if r.status_code == 200:
                    print(f"{done}Đã xoá file {file_name} thành công.")
                else:
                    print(f"{error}Lỗi khi xoá file:", r.json())
            else:
                print("Đã huỷ xoá file.")
        except (IndexError, ValueError):
            print(f"Lựa chọn không hợp lệ.")
    else:
        print("Không thể lấy danh sách file:", r.json())

def delete_repo(headers, username, current_repo):
    repos = requests.get(f"https://api.github.com/user/repos", headers=headers).json()
    if not repos:
        print(f"Bạn không có repo nào để xoá.")
        return current_repo
    minhanhs()
    print(f"\n{kt}  Danh sách repo:")
    for idx, repo in enumerate(repos):
        print(f"  {kt}{xla} Repo {idx+1}{trang}: {vang}{repo['name']}")

    choice = input(f"Nhập số thứ tự repo muốn xoá: ").strip()
    try:
        idx = int(choice) - 1
        repo_name = repos[idx]['name']

        confirm = input(f"Bạn có chắc muốn xoá repo '{repo_name}'(y/n): ").strip().lower()
        if confirm == 'y':
            url = f"https://api.github.com/repos/{username}/{repo_name}"
            r = requests.delete(url, headers=headers)
            if r.status_code == 204:
                print(f"{done} Đã xoá repo '{repo_name}' thành công.")
                if repo_name == current_repo:
                    print(f"Repo hiện tại đã bị xoá, chọn repo mới.")
                    return ma_repo(headers, username)
                else:
                    return current_repo
            else:
                print(f"{error}Lỗi khi xoá repo:", r.status_code, r.text)
                return current_repo
        else:
            print(f"{error}{do}Đã huỷ xoá repo.")
            return current_repo
    except (IndexError, ValueError):
        print("Lựa chọn không hợp lệ.")
        return current_repo

def main():
    headers, username = ma_git()
    repo = ma_repo(headers, username)

    while True:
        minhanhs()
        print(f"\n[Repo hiện tại: {repo}]")
        print("1. Upload - Tạo file mới")
        print("2. Đổi repo")
        print("3. Xoá file")
        print("4. Xoá repo")
        print("5. Thoát")
        choice = input(f"Nhập lựa chọn: ").strip()

        if choice == '1':
            ma_up_file(headers, username, repo)
        elif choice == '2':
            repo = ma_repo(headers, username)
        elif choice == '3':
            delete_file(headers, username, repo)
        elif choice == '4':
            repo = delete_repo(headers, username, repo)
        elif choice == '5':
            print(f"Cảm ơn! Chúc bạn dùng tool vui vẻ")
            break
        else:
            print(f"{error}Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()