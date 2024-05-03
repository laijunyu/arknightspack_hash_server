import hashlib
import requests
def download_file_with_requests(url, save_path):  
    response = requests.get(url, stream=True)  
    response.raise_for_status()  # 如果请求失败则抛出HTTPError异常  
  
    with open(save_path, 'wb') as file:  
        for chunk in response.iter_content(chunk_size=8192):  
            if chunk:  
                file.write(chunk)  
  
# 使用方法  
url = 'http://example.com/somefile.zip'  
save_path = 'path/to/your/directory/somefile.zip'  # 替换为你想要保存文件的路径  
download_file_with_requests(url, save_path)

def hash_file(file_path):  
    # 打开文件以二进制模式读取  
    with open(file_path, 'rb') as file:  
        # 读取文件内容并计算哈希  
        md5_hash = hashlib.md5()  
        while True:  
            # 读取块数据（这里使用4096字节的块大小）  
            data = file.read(4096)  
            if not data:  
                break  
            # 更新哈希对象  
            md5_hash.update(data)  
    # 获取哈希的十六进制表示形式  
    md5_name = md5_hash.hexdigest()  
    return md5_name  
  
# 调用函数，传入一个真实的文件路径  
hash_result = hash_file("C:\\Users\\29581\\Documents\\Downloads\\1.exe")  # 替换为你的文件路径  
print(hash_result)
