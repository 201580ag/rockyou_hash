# 입력 파일 경로 정의
input_file_md5 = "MD5-rockyou.txt"
input_file_sha256 = "SHA256-rockyou.txt"
input_file_sha512 = "SHA512-rockyou.txt"

# 사용자로부터 입력 받은 해시
user_input_hash = input("찾고자 하는 해시를 입력하세요: ")

# MD5 파일에서 찾기
with open(input_file_md5, "r", encoding="utf-8") as file_md5:
    for line in file_md5:
        parts = line.strip().split(":")
        if len(parts) == 2:
            md5_hash, password = parts[0], parts[1]
            if user_input_hash == md5_hash:
                print(f"MD5 해시 '{user_input_hash}'에 대한 비밀번호: {password}")
                break
    else:
        print("MD5에서 해시를 찾을 수 없습니다.")

# SHA-256 파일에서 찾기
with open(input_file_sha256, "r", encoding="utf-8") as file_sha256:
    for line in file_sha256:
        parts = line.strip().split(":")
        if len(parts) == 2:
            sha256_hash, password = parts[0], parts[1]
            if user_input_hash == sha256_hash:
                print(f"SHA-256 해시 '{user_input_hash}'에 대한 비밀번호: {password}")
                break
    else:
        print("SHA-256에서 해시를 찾을 수 없습니다.")

# SHA-512 파일에서 찾기
with open(input_file_sha512, "r", encoding="utf-8") as file_sha512:
    for line in file_sha512:
        parts = line.strip().split(":")
        if len(parts) == 2:
            sha512_hash, password = parts[0], parts[1]
            if user_input_hash == sha512_hash:
                print(f"SHA-512 해시 '{user_input_hash}'에 대한 비밀번호: {password}")
                break
    else:
        print("SHA-512에서 해시를 찾을 수 없습니다.")
