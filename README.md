# 14기 대전 1반 알고리즘 스터디

> 하루 1문제씩 꾸준히, 화/목엔 코드 리뷰!  
> 알고리즘 실력을 함께 키워나가는 스터디입니다 💪

## 참여자

> | 이름 | GitHub ID |
> | --- | --- |
> | 강보희 | bohuiKang |
> | 강찬휘 | kch0324 |
> | 김도연 | dy2kim |
> | 변아영 | Ayeong-99 |
> | 하지연 | wldus021128 |


## 📅 스터디 운영 방식

### ✅ 문제 풀이
- 월~일 매일 1문제 풀이(기본)

#### IM1단계 문제는 아래와 같이 진행
- 월~금 매일 2문제 풀이
- 토~일 매일 3문제 풀이

- 폴더 이름: `aug_week1`, `aug_week2` 등 날짜 형식
- ~~각자 자신의 폴더에 파일 업로드 (예: `aug_week1/boj_1000/user1.py`)~~
- 각자 자신의 폴더에 파일 업로드 (예: `aug_week1/user1/boj_1000.py`)
- https://www.acmicpc.net/group/workbook/23989

### ✅ 코드 리뷰
- 화/목 코드 리뷰 및 과목/월말 평가 준비

## 💾 코드 업로드 방식

```
[스터디장]
1. Repo 생성 → 초기 디렉토리 → 첫 푸시 → 팀원 추가

[팀원]
1. Repo 클론 → 개인 브랜치 생성
2. 문제 풀이 → add/commit/push
3. PR 생성

[스터디장]
1. PR 리뷰 → Merge → main 최신화
2. 팀원들에게 main pull 안내

[팀원]
1. main pull & 개인 브랜치 merge → 다음 문제 풀이 반복
```

### ✅ 클론 & 브랜치 생성
- 리포지토리 클론
```bash
git clone <repo-url>
cd algo-study
```
- 각자 본인 이름(or 아이디) 브랜치 생성
```bash
git checkout -b bohui
```
- 자신의 브랜치에서만 작업 (main에는 직접 푸시 ❌)

### ✅ 문제 풀이 후
- 변경사항 커밋
```bash
git add aug_week1/bohui/boj_1000.py
git commit -m "bohui: BOJ 1000번 풀이 추가"
```
- 원격 브랜치로 푸시
```bash
git push origin bohui
```
- GitHub에서 Pull Request (PR) 생성
  - GitHub → Compare & Pull Request 클릭
  - PR 제목: [bohui] week1 day1 풀이 제출
  - 내용: 간단한 풀이 설명 (선택)

### ✅ 스터디장이 할 일
- GitHub에서 PR 확인
- 코드 리뷰(코멘트) → 승인(Approve)
- 문제 없으면 main 브랜치에 Merge
- Merge 후 팀원들에게 main 최신화 안내

### ✅ 팀원들은 다음 작업 전에 항상 main 최신화
- 새로운 작업 시작 전
```bash
git checkout main
git pull origin main
git checkout bohui
git merge main
```
