# auto-stock-trading-system
Auto stock trading system with python
___

[정리]

## 개미들이 시장에서 성공할 수 없는 이유
1. 정보의 부족
2. 시간의 부족

## 알고리즘 트레이딩(Algorithmic Trading)
1. 전날의 거래 패턴(거래량, 종가, 시가, 주식 가격 변동 폭 등)을 분석 -> 투자 유망 종목 추천
2. 자동 주식 거래

- 필수 요소 : 투자노하우(알고리즘) => 방대한 정보의 분석

## 알고리즘 트레이딩 전략

### 추세 추종형 전략 (Trend Following Strategies)
기술적 지표와 관련된 이동평균선, 채널 브레이크아웃, 가격 수준 변화에 대한 추세를 따르는 가장 보편적인 알고리즘 트레이딩 전략
가격에 대한 예상을 하지 않으므로 구현하기에 매우 쉽고 간단
거래는 요구되는 추세의 출현에 기초하여 일어나며, 예측 분석의 복잡성없이 알고리즘을 쉽고 직관적으로 구현
(50일- 200일 이동평균선 예제)

### 차익 기회 (Arbitrage Opportunities)
한 시장에서 낮은 가격에 주식을 매수하여 다른 시장에서 비싼 가격에 동시에 매도하는 것
주식의 선물 시장 또한 시간에 따라 가격이 변화하므로 같은 원리 적용가능

### 수학적 모델 기반 전략
옵션과 파생된 증권의 조합의 거래를 통해 +델타와 -델타로 포트폴리오의 델타를 0이 되도록 유지하는 Delta-neutral 트레이딩 전략

### 범위 거래 (평균 회귀. Mean Reversion)
평균 회귀(Mean Reversion)전략은 자산의 높고 낮은 가격이 일시적인 현상이며 곧 그들의 평균 가격으로 돌아올 것이라는 가정
가격 범위를 확인하고 정의하며, 이 가정에 기초하여 알고리즘을 구현하는 것으로 가격이 정의된 범위에 들어오거나 벗어날 때 주문 자동 수행

### 거래량 가중평균 가격 (Volume Weighted Average Price. VWAP)
거대한 주문을 주식의 특정 거래량에 따라 잘게 나누어, 거래량 가중평균 가격(VWAP)에 가깝게 주문을 실행하여 평균 가격으로 부터 수익을 얻음

### 시간 가중평균 가격 (Time Weighted Average Price. TWAP)
거대한 주문을 시작과 종료 시점 사이에 일정하게 시간을 나눈 슬롯을 따라 잘게 나누어, 시작 및 종료 시점 사이의 평균 가격에 가깝게 주문을 수행하여 시장의 영향을 최소화

### 거래량 비율 (Percentage of Volume. POV)
거래 주문이 완전히 체결될 때까지 이 알고리즘은 미리 정의된 비율과 시장에서 거래되는 거래량에 따라 계속해서 부분적인 주문을 수행.
연관된 “단계 전략”은 주식의 가격이 사용자가 정의한 수준에 도달했을 때 미리 정의한 시장 거래량의 퍼센티지와 참여 비율을 증가시키거나 감소시키면서 주문

### 임플리멘테이션 숏폴 (Implementation Shortfall)
실시간 시장에서 (주문)실행 비용을 최소화하는 목표. 지연된 실행의 기회 비용을 통해 주문 비용을 절약.
주식의 가격이 유리하게 흐르면 목표 참여 비율을 증가시키고 가격이 안좋게 흐르면 비율을 감소

## 알고리즘 검증(백테스팅)


___
[패키지 구성]

- conf : 사용자 정보 저장  
- agent : 수집, 매매, 지원 모듈  
- db_handler : DB저장, 변경 지원 모듈  
- scheduler : 스케줄러 모듈  

___

**win32 호환성 문제**   
pywin32	(win32com) -> 32bit에서만 작동   
anaconda bit 설정 변경 => set CONDA_FORCE_32BIT=1  

**파일명 mismatch**   
ex) "t1305.res"를 "t1305 .res"로 찾으려고 함   
xa_query.LoadFromResFile(XAQuery.RES_PATH + res + **" .res"**) 코드 수정  

**gitignore 캐시 제거**  
git rm -r --cached .   
git add .   
git commit -m "Fix untracked files"   