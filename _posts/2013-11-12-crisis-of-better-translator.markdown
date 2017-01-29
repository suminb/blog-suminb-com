---
layout: post
title: 더 나은 번역기의 위기
categories:
- Software Engineering
- Troubleshooting
tags: []
status: publish
type: post
published: true
meta:
  _edit_last: '1'
  dsq_thread_id: '1967235215'
author:
  login: admin
  email: suminb@gmail.com
  display_name: Sumin
  first_name: Sumin
  last_name: Byeon
redirect_to:
  - http://philosophical.one/post/crisis-of-better-translator
---
[더 나은 번역기][btr] 장사 망할뻔 했다.

새벽 2시쯤이었나? [Hallucination][hallucination] 서비스에서 사용하는 프록시 서버들의 상태를 살펴보고 있었는데, 적중률(hit ratio) 값이 형편 없는 수준으로 곤두박질 치고 있었다. 아니 이게 무슨 일인가(!) 싶어서 [번역기][btr]를 열어서 확인해봤더니 역시나 빨간 글씨로 줄기차게 에러 메세지를 뱉어내고 있었다.

구글에서 뭔가 정책을 바꿨는지 프록시 서버를 통해서 번역 요청을 하면 CAPTCHA[^2]를 요구하는 것이었다. 또, GET으로 요청을 보냈을 때와 POST로 요청을 보냈을 때 각각 다른 현상이 나타나기도 하고, 새로 바뀐 매개변수 이름[^3]도 있어서 다시 리버스 엔지니어링을 해야 할 판이었다. 여러가지 임시 해결책을 시도해봤지만, 아예 작동이 되지 않거나 채 한 시간을 넘기지 못하고 HTTP 503 메세지를 뱉어내는 것이었다.

어느새 새벽 4시를 넘긴 시간. 나는 선택의 기로에 놓였다. 돈도 안 되는 망할놈의 [번역기][btr] 되던지 말던지 내버려 두고 잠이나 잘 것인지, 아니면 프로그래머로서, 그리고 컴퓨터 과학자(computer scientist)로서 꺼져가는 열정을 다시 되찾게 해준 고마운 존재인 [번역기][btr]를 되살려 놓을것인지. 사실 이번 학기 세미나 수업에서 발표 하고 페이퍼 쓰는것도 번역기 프로젝트에서 나온 부산물(bilingual corpus based cross-language information retrieval)을 이용하고 있고, YGTLC 컨퍼런스 신청서도 이걸 기반으로 썼기 때문에 쉽게 포기할 수는 없었다.

그러다가 문득 얼마 전에 [ChiHyun Lim](https://www.facebook.com/chihyun.lim)이 보여줬던 [goxcors][] 프로젝트가 떠올랐다. 아, 이거면 되겠구나. 다행히도 구글 앱 엔진에 바로 디플로이 할 수 있도록 만들어진 코드라서 디플로이 하는데 채 15분도 걸리지 않았다. 그 다음, 번역기 프로젝트 저장소에 브랜치를 하나 만들고 [goxcors][]를 이용해서 [번역기][btr]가 작동할 수 있도록 소스코드를 수정하기 시작했다. 새벽 시간에만 나오는 초인적인 힘으로 코딩을 하니 음악 소리도, 기차 소리도, 아무것도 들리지 않고 코드만 보이는 해탈의 경지에 이르렀다. 잠깐이었겠지만.

아, 이제 빨간 글씨가 보이지 않는다. [번역기][btr]가 정상으로 돌아왔다. 약간의 약식 테스트를 거친 후, 고도로 훈련된 원숭이가 문제를 해결하고 있다는 메세지[^5]를 내리고 다시 [번역기][btr] 사이트를 활성화 시켰다. 다 해결하고 나니까 어느새 6시 반이었다. 창밖에서는 해가 떠오르고 있고 새 소리가 들려오고 있었다. 문제를 해결했다는 안도감 때문이었는지 난 침대에 눕자마자 잠들었다.[^6]

덧. 늦잠을 자는 바람에 오늘 첫 수업은 빠지게 됐다.

[^2]: 요청자가 실제 사람인지 구분하기 위해서 컴퓨터가 인식하기 어려운 숫자나 문자 등을 보여주고 그 내용을 물어보는 인증 방법.
[^3]: 하위 호환성을 위해서 그랬겠지만, 바뀌기 이전의 이름을 써도 아직은 정상 작동한다.
[^5]: http://maintenance.suminb.com/
[^6]: 사실 평소에도 그런다.
[btr]: http://better-translator.com
[hallucination]: https://github.com/suminb/hallucination
[goxcors]: https://github.com/acidsound/goxcors
