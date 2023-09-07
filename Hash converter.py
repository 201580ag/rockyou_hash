import hashlib
from tqdm import tqdm
import os

# 입력 파일과 출력 파일 경로 정의
input_file = "rockyou.txt"
output_file_md5 = "MD5-rockyou.txt"
output_file_sha256 = "SHA256-rockyou.txt"
output_file_sha512 = "SHA512-rockyou.txt"

# 입력 파일의 크기 확인
input_file_size = os.path.getsize(input_file)  # 바이트 단위로 크기 가져오기

# 입력 파일의 총 라인 수 계산 (진행 상황 표시용)
with open(input_file, "r", encoding="utf-8", errors="ignore") as input:
    total_lines = sum(1 for line in input)

# 출력 파일 열기 (UTF-8 인코딩으로)
with open(output_file_md5, "w", encoding="utf-8") as output_md5, \
     open(output_file_sha256, "w", encoding="utf-8") as output_sha256, \
     open(output_file_sha512, "w", encoding="utf-8") as output_sha512:

    # 입력 파일 열기 (UTF-8 인코딩으로)
    with open(input_file, "r", encoding="utf-8", errors="ignore") as input:
        for line in tqdm(input, total=total_lines, desc="Converting", unit=" lines", unit_scale=True,
                         ncols=100, ascii=True, mininterval=0.1):
            password = line.strip()  # 줄 바꿈 문자 제거
            # MD5 해시 생성
            md5_hash = hashlib.md5(password.encode()).hexdigest()
            # SHA-256 해시 생성
            sha256_hash = hashlib.sha256(password.encode()).hexdigest()
            # SHA-512 해시 생성
            sha512_hash = hashlib.sha512(password.encode()).hexdigest()

            # 각 해시와 원본 비밀번호를 각각의 출력 파일에 쓰기
            output_md5.write(f"{md5_hash}:{password}\n")
            output_sha256.write(f"{sha256_hash}:{password}\n")
            output_sha512.write(f"{sha512_hash}:{password}\n")

# 출력 파일의 크기 확인
output_file_md5_size = os.path.getsize(output_file_md5)  # 바이트 단위로 크기 가져오기
output_file_sha256_size = os.path.getsize(output_file_sha256)  # 바이트 단위로 크기 가져오기
output_file_sha512_size = os.path.getsize(output_file_sha512)  # 바이트 단위로 크기 가져오기

print(f"비밀번호를 MD5 해시로 변환하여 '{output_file_md5}' 파일에 저장했습니다.")
print(f"비밀번호를 SHA-256 해시로 변환하여 '{output_file_sha256}' 파일에 저장했습니다.")
print(f"비밀번호를 SHA-512 해시로 변환하여 '{output_file_sha512}' 파일에 저장했습니다.")
print(f"입력 파일 크기: {input_file_size} 바이트")
print(f"MD5 출력 파일 크기: {output_file_md5_size} 바이트")
print(f"SHA-256 출력 파일 크기: {output_file_sha256_size} 바이트")
print(f"SHA-512 출력 파일 크기: {output_file_sha512_size} 바이트")
