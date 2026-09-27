# TwinRich Notes — Blogger 발행 런북 (맥북 불필요)

블로그: https://twinrichnote.blogspot.com (영어, 세계 독자 대상)
발행 경로: Gmail(dosik99@gmail.com) → Blogger 비밀 게시 주소(이메일 즉시 게시). 주소는 발행 작업 설정에만 두고 이 저장소에 적지 않는다.
이미지 경로: 이 저장소 `posts/`에 PNG를 올리고, 글 HTML에서 아래 주소로 불러온다.
`https://raw.githubusercontent.com/dosik1977/twinrichnote-images/main/posts/<slug>.png`

## 글 1편 절차
1. 주제 선정: 최근 공식 1차 출처(SEC/Investor.gov, Fed, NASA, JEDEC, 기업 IR 등). 게시된 글과 중복 금지.
2. 사실 확인: 모든 수치·날짜는 1차 출처를 직접 열어 확인. 확인 못 한 내용은 쓰지 않는다. 가상 예시는 가상이라고 명시. 투자 권유 금지.
3. 이미지(필수, 글마다 최소 1장): `python3 tools/make_card.py tools/specs/<slug>.json posts/<slug>.png` (1536x1024, 영어, badge "Conceptual illustration · Not investment advice"). 생성 후 이미지를 직접 열어 글자 넘침이 없는지 확인.
4. 커밋·푸시 후 raw 주소가 200과 image/png를 돌려주는지 curl로 확인.
5. HTML 본문: 도입 2문단 → `<p><img src="RAW주소" alt="설명" style="max-width:100%;height:auto"></p>` → 첫 `<h2>`. 끝에 공식 출처 링크와 해시태그 8개 안팎.
6. 이메일 첨부파일로 이미지를 보내지 않는다(텍스트로 옮기다 깨진다). 이미지는 반드시 위 주소로만 넣는다.
7. 발행 후 `https://twinrichnote.blogspot.com/feeds/posts/summary?alt=json`으로 게시 확인. 같은 글을 다시 보내지 않는다(이메일 게시는 수정 불가, 재전송=중복). 문제가 있으면 사용자에게 보고만 한다.
