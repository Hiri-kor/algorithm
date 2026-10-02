"""레포 안의 모든 풀이를 읽어서 목록 README.md와 problems.json을 만든다.
지원: SWEA, 프로그래머스 (백준허브가 올린 README 형식)

사용법: 레포 최상위에서  python scripts/build_index.py
"""
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/Hiri-kor/algorithm/tree/main"

# 백준허브 README 첫 줄 예:
#   SWEA        "# [D1] 홀수만 더하기 - 2072"
#   프로그래머스  "# [level 0] 문자열 출력하기 - 181952"
# \s 는 일반 공백뿐 아니라 백준허브가 쓰는 특수 공백(U+2005)도 잡는다.
HEADER_RE = re.compile(r"^#\s*\[(.+?)\]\s*(.+?)\s*-\s*(\d+)\s*$")
DATE_RE = re.compile(r"### 제출 일자\s+(.+)")

# 사이트마다 날짜 형식이 다르다.
#   SWEA        "2026-10-01 21:50"
#   프로그래머스  "2026년 10월 02일 12:20:20"
DATE_FORMATS = ["%Y-%m-%d %H:%M", "%Y년 %m월 %d일 %H:%M:%S"]

INTRO = "SWEA · 프로그래머스 알고리즘 풀이 기록 (Python)"

COPYRIGHT = """## 저작권 안내

- 각 문제의 문제 설명, 입출력 예시 등 문제 원문의 저작권은 해당 출처에 있습니다.
  - SWEA 문제: [SW Expert Academy](https://swexpertacademy.com)
  - 프로그래머스 문제: [프로그래머스](https://school.programmers.co.kr)
- 이 저장소의 풀이 코드는 학습 목적으로 작성한 것이며, 각 문제 폴더의 README에 원문 링크와 출처를 함께 적었습니다.
- 저작권자의 요청이 있으면 해당 내용을 바로 삭제하겠습니다."""


def parse_date(text):
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text.strip(), fmt)
        except ValueError:
            pass
    return None


def short_level(level):
    """'level 0' → 'Lv.0', 'D1' → 'D1'"""
    m = re.fullmatch(r"level\s*(\d+)", level, re.I)
    return f"Lv.{m.group(1)}" if m else level


def level_sort_key(level):
    """D1, D2 ... / Lv.0, Lv.1 ... 을 숫자 순서로 정렬하기 위한 키"""
    m = re.search(r"\d+", level)
    return (int(m.group()) if m else 999, level)


def parse_problem(readme_path):
    """문제 폴더의 README.md 하나를 읽어 정보를 딕셔너리로 돌려준다.
    형식이 예상과 다르면 None을 돌려준다."""
    text = readme_path.read_text(encoding="utf-8")
    first_line = text.splitlines()[0].strip() if text else ""

    header = HEADER_RE.match(first_line)
    date_match = DATE_RE.search(text)
    if not header or not date_match:
        return None
    date = parse_date(date_match.group(1))
    if date is None:
        return None

    level, title, number = header.groups()
    folder = readme_path.parent.relative_to(ROOT)
    return {
        "site": folder.parts[0],          # 맨 위 폴더 이름: SWEA, 프로그래머스
        "level": short_level(level),
        "title": title,
        "number": number,
        "date": date.strftime("%Y-%m-%d %H:%M"),
        "url": f"{REPO_URL}/{quote(folder.as_posix())}",
    }


def collect_problems():
    """<사이트>/<난이도>/<문제 폴더>/README.md 를 모두 찾아 파싱한다."""
    problems = []
    for readme in sorted(ROOT.glob("*/*/*/README.md")):
        if any(p.startswith(".") for p in readme.relative_to(ROOT).parts):
            continue  # .github 같은 숨김 폴더는 건너뜀
        info = parse_problem(readme)
        if info is None:
            print(f"[건너뜀] 형식이 다름: {readme.relative_to(ROOT)}")
            continue
        problems.append(info)
    return problems


def build_readme(problems):
    lines = [
        "# algorithm",
        "",
        INTRO,
        "",
        "<!-- 이 파일은 scripts/build_index.py가 자동으로 만듭니다. 직접 고치면 다음 갱신 때 덮어써집니다. -->",
        "",
    ]
    if not problems:
        lines += ["아직 기록된 문제가 없습니다.", "", COPYRIGHT, ""]
        return "\n".join(lines)

    # {사이트: {난이도: [문제, ...]}}
    tree = {}
    for p in problems:
        tree.setdefault(p["site"], {}).setdefault(p["level"], []).append(p)

    summary = " · ".join(f"{site} {sum(len(v) for v in tree[site].values())}" for site in sorted(tree))
    lines += [f"**총 {len(problems)}문제** ({summary})", "", "아래 항목을 누르면 펼쳐집니다.", ""]

    # 사이트별로 한 번, 그 안에서 난이도별로 한 번 더 접는다.
    # <summary> 다음과 </details> 앞에 빈 줄이 있어야 안쪽 마크다운 표가 제대로 그려진다.
    for site in sorted(tree):
        site_total = sum(len(v) for v in tree[site].values())
        lines += ["<details>", f"<summary><b>{site}</b> ({site_total}문제)</summary>", ""]
        for level in sorted(tree[site], key=level_sort_key):
            items = sorted(tree[site][level], key=lambda p: int(p["number"]))
            lines += [
                "<details>",
                f"<summary>{level} ({len(items)})</summary>",
                "",
                "| 번호 | 문제 | 푼 날짜 |",
                "| --- | --- | --- |",
            ]
            for p in items:
                lines.append(f"| {p['number']} | [{p['title']}]({p['url']}) | {p['date'][:10]} |")
            lines += ["", "</details>", ""]
        lines += ["</details>", ""]

    lines += [COPYRIGHT, ""]
    return "\n".join(lines)


def write_if_changed(path, content):
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def main():
    problems = collect_problems()
    problems.sort(key=lambda p: p["date"], reverse=True)  # json은 최신순

    changed = write_if_changed(ROOT / "README.md", build_readme(problems))
    changed |= write_if_changed(
        ROOT / "problems.json",
        json.dumps(problems, ensure_ascii=False, indent=2) + "\n",
    )
    print(f"총 {len(problems)}문제, {'갱신함' if changed else '변경 없음'}")


if __name__ == "__main__":
    main()
