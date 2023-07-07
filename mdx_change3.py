import os
import random
import shutil


def modify_and_move_files(original_dir, target_dir):
    # 폴더가 없다면 생성
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    if not os.path.exists(target2_dir):
        os.makedirs(target2_dir)

    for filename in os.listdir(original_dir):
        if filename.endswith(".mdx"):
            new_filename = os.path.join(target_dir, filename)
            with open(os.path.join(original_dir, filename), "r", encoding="utf-8") as f:
                lines = f.readlines()
                with open(new_filename, "w", encoding="utf-8") as new_f:
                    # 첫 5줄은 그대로 작성
                    for i in range(5):
                        new_f.write(lines[i])
                    # 나머지 줄은 처리
                    for line in lines[5:]:
                        # '.'로 분할하고, 각 문장에 줄바꿈을 추가하여 다시 합침
                        if not line.startswith("#"):
                            sentences = line.split(". ")
                            new_line = ". \n".join(sentences)
                            new_f.write(new_line)
                        else:
                            new_f.write(line)
            # 원래 디렉토리의 파일 삭제
    for filename in os.listdir(target_dir):
        if filename.endswith(".mdx"):
            new_filename = os.path.join(target2_dir, filename)
            with open(os.path.join(target_dir, filename), "r", encoding="utf-8") as f:
                lines = f.readlines()
                with open(new_filename, "w", encoding="utf-8") as new_f:
                    # 첫 5줄은 그대로 작성
                    for i in range(5):
                        new_f.write(lines[i])
                    # 나머지 줄은 처리
                    for line in lines[5:]:
                        line = line.replace("요:", "요").replace("다:", "다")
                        # '.'로 분할하고, 각 문장에 줄바꿈을 추가하여 다시 합침
                        if line.startswith("#"):
                            new_f.write(line)
                        elif line.strip() == "":
                            new_f.write(line)
                        else:
                            line = line.replace("하세요", "할 것")
                            line = line.replace("기울이세요", "기울일 것")
                            line = line.replace("바르십시오", "바를 것")
                            line = line.replace("따르십시오", "따를 것")
                            line = line.replace("둡니다", "둠")
                            line = line.replace("돕습니다", "도움")
                            line = line.replace("시키세요", "시킬 것")
                            line = line.replace("주세요", "줄 것")
                            line = line.replace("배웁니다", "배울 것")
                            line = line.replace("다듬습니다", "다듬을 것")
                            line = line.replace("냅니다", "낼 것")
                            line = line.replace("봅니다", "볼 것")
                            line = line.replace("합니다", "함")
                            line = line.replace("있습니다", "있음")
                            line = line.replace("입니다", "임")
                            line = line.replace("됩니다", "됨")
                            line = line.replace("내리세요", "내려야 함")
                            line = line.replace("좋습니다", "좋음")
                            line = line.replace("하십시오", "해야함")
                            line = line.replace("시킵니다", "시킴")
                            line = line.replace("줍니다", "줌")
                            line = line.replace("으세요", "을 것")
                            line = line.replace("마세요", "말 것")
                            line = line.replace("보세요", "볼 것")
                            line = line.replace("두세요", "둘 것")
                            line = line.replace("높습니다", "높음")
                            line = line.replace("낮습니다", "낮음")
                            line = line.replace("따릅니다", "따름")
                            line = line.replace("받습니다", "받음")
                            line = line.replace("으십시오", "을 것")
                            line = line.replace("갑니다", "감")
                            line = line.replace("즐기세요", "즐길 것")
                            line = line.replace("갑니다", "갈 것")
                            new_f.write(line)

# 현재 스크립트의 위치를 찾음
current_script_path = os.path.dirname(os.path.abspath(__file__))

# 현재 스크립트의 위치를 기준으로 original_dir 경로를 설정
original_dir = os.path.join(current_script_path, 'posts')
target_dir = os.path.join(current_script_path, 'zz')
target2_dir = os.path.join(current_script_path, 'zz2')

modify_and_move_files(original_dir, target_dir)
