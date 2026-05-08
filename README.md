# iCUVE 자동화 시스템 V1

> 공연제작사 아이큐브(iCUVE)의 뉴스레터 발송 자동화 플랫폼

**Developed by 김달미**

---

## 📌 개요

공연 현장 사진과 기본 정보를 입력하면 AI가 자동으로 뉴스레터 본문을 작성하고, 수신자 목록에 이메일을 일괄 발송하는 통합 자동화 시스템입니다.

---

## ✨ 주요 기능

- **AI 본문 자동 작성** — 공연명, 날짜, 장소, 관객수, 발주처 입력 시 Claude AI가 자동으로 뉴스레터 본문 생성
- **사진 분석** — 업로드한 공연 현장 사진을 AI가 직접 분석하여 현장감 있는 글 작성
- **글 용도 / 톤 선택** — 보고용 / 홍보용 / SNS용, 공식적 / 따뜻한 / 세련된 톤 선택 가능
- **Quill 에디터** — AI가 작성한 글을 자유롭게 수정 가능한 리치 텍스트 에디터
- **이미지 자동 업로드** — Cloudinary 연동으로 사진 최대 5장 자동 업로드 및 날짜별 폴더 관리
- **하이라이트 영상** — YouTube / 네이버 클립 링크 첨부 및 썸네일 자동 표시
- **수신자 관리** — CSV 업로드 또는 직접 추가로 수신자 관리
- **일괄 발송** — Gmail SMTP를 통한 개인화 이메일 일괄 발송
- **모바일 지원** — 현장에서 모바일로도 바로 사용 가능한 반응형 디자인

---

## 🛠 기술 스택

| 구분 | 기술 |
|------|------|
| 프론트엔드 | HTML / CSS / JavaScript |
| 에디터 | Quill.js |
| 호스팅 | GitHub Pages |
| 백엔드 | Python (Flask) |
| 서버 배포 | Render |
| AI | Anthropic Claude API |
| 이미지 호스팅 | Cloudinary |
| 이메일 발송 | Gmail SMTP |

---

## 📁 파일 구조

```
icuve-server/
├── index.html         # 메인 UI (GitHub Pages로 배포)
├── server.py          # Flask 백엔드 서버 (Render로 배포)
└── requirements.txt   # Python 패키지 목록
```

---

## 🚀 사용 방법

1. [iCUVE 자동화 시스템](https://iamninesoup.github.io/icuve-server/) 접속
2. Cloudinary 설정 입력 (최초 1회)
3. 수신자 CSV 업로드 또는 직접 추가
4. 메일 제목 입력
5. 공연 정보 입력 후 **✨ AI로 본문 자동 작성** 클릭
6. 공연 사진 업로드 (최대 5장)
7. 하이라이트 영상 링크 입력 (선택)
8. 미리보기 확인 후 **📨 뉴스레터 발송**

---

## ⚙️ 환경 설정

### Render 환경변수
```
CLAUDE_API_KEY=your_claude_api_key
```

---

## 📅 업데이트 예정

- [ ] 블로그 글 자동 생성
- [ ] YouTube 자동 업로드
- [ ] 숏폼 자동 편집
- [ ] 네이버 블로그 복붙용 포맷 출력

---

© 2026 iCUVE. Developed by 김달미.
