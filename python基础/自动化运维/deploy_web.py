import os
import wget
import requests
import hashlib
import tarfile

def has_new_ver(ver_fname, ver_url):
    if not os.path.exists(ver_fname):
        return True

    with open(ver_fname) as f:
        local_ver = f.read()
    r = requests.get(ver_url)

    if local_ver != r.text:
        return True

    return False

def file_ok(app_fname, md5_url):
    m = hashlib.md5()

    with open(app_fname, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
    r = requests.get(md5_url)

    if m.hexdigest() == r.text.strip():
        return True
    return False

def deploy(app_fname, deploy_dir, dest):
    tar = tarfile.open(app_fname)
    tar.extractal(path=deploy_dir)
    tar.close

    app_dir = os.path.basename(app_fname)
    app_dir = app_dir.replace(".tar.gz")
    app_dir = os.path.join(deploy_dir, app_dir)

    if os.path.exists(dest):
        os.remove(dest)
    os.symlink(app_dir, dest)

if __name__ == '__main__':
    # 判断服务器是否有新版本
    ver_url = 'http://127.0.0.1/deploy/live_ver'
    ver_fname = "/var/www/deploy/live_ver"
    if not has_new_ver(ver_fname, ver_url):
        print("无更新")
        exit(1)
    
    # 下载新版本
    tag = requests.get(ver_url)
    app_url = f"http://127.0.0.1/deploy/pakgs/mysite-{tag.text}.tar.gz"
    app_fname = f"/var/www/download/mysite-{tag.text}.tar.gz"
    wget.download(app_url, app_fname)

    # 校验下载压缩包
    md5_url = app_url+".md5"
    if not file_ok(app_fname, md5_url):
        print("已损坏")
        os.remove(app_fname)
        exit(2)
    
    # 部署软件到web服务器
    deploy_dir = "/var/www/deploy"
    dest = "/var/www/html/current"
    deploy(app_fname, deploy_dir, dest)

    # 更新本地文件
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)