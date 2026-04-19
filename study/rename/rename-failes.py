import os
import re
import math


def get_rename_list(directory_path, prefix):
    """
    파일 개수에 따라 자릿수를 자동 계산하여 리네임 리스트 생성
    """
    # 1. 파일 목록 필터링 (숨김 파일 등 제외)
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # 2. Natural Sort (숫자 순 정렬)
    def natural_key(string_):
        return [int(s) if s.isdigit() else s.lower() for s in re.split('([0-9]+)', string_)]

    files.sort(key=natural_key)

    # 3. 자릿수 자동 계산 (예: 150개 파일 -> 3자리)
    total_files = len(files)
    if total_files == 0:
        return []

    # log10을 이용해 필요한 자릿수 계산 (최소 2자리 유지 권장)
    padding = max(2, math.ceil(math.log10(total_files + 1)))

    rename_plan = []
    for index, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1]

        # 새 이름 생성: prefix + 자동 자릿수 숫자 + 확장자
        new_name = f"{prefix}{index:0{padding}d}{ext}"

        old_path = os.path.join(directory_path, filename)
        new_path = os.path.join(directory_path, new_name)

        rename_plan.append((old_path, new_path))

    return rename_plan


def execute_rename(rename_plan):
    print(f"{'--- 리네임 작업을 시작합니다 ---':^40}")
    success_count = 0
    for old, new in rename_plan:
        try:
            os.rename(old, new)
            print(f"[성공] {os.path.basename(old)} -> {os.path.basename(new)}")
            success_count += 1
        except Exception as e:
            print(f"[실패] {os.path.basename(old)}: {e}")
    print(f"--- 작업 완료: {success_count}개 파일 변경됨 ---")


# --- 실행 로직 ---
target_directory = "/Volumes/T7/study/japan/n4/n4-grammar"
file_prefix = "n4_grammar_"  # 원하는 접두사 설정

plan = get_rename_list(target_directory, file_prefix)

if not plan:
    print("변경할 파일이 없습니다.")
else:
    print(f"총 {len(plan)}개의 파일을 찾았습니다.")
    print("--- 변경 예정 목록 (미리보기) ---")
    # 목록이 너무 길 수 있으므로 상위 10개만 출력하거나 전체 출력 선택
    for old, new in plan[:10]:
        print(f"{os.path.basename(old)} \t >> \t {os.path.basename(new)}")
    if len(plan) > 10: print("...")

    confirm = input(f"\n[{file_prefix}] 형식으로 자릿수를 맞춰 변경하시겠습니까? (y/n): ")
    if confirm.lower() == 'y':
        execute_rename(plan)
    else:
        print("작업이 취소되었습니다.")