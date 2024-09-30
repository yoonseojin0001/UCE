--- 논문 코드 질문 ---
논문 코드에서 이해가 되지 않는 부분을 일단 제외했습니다.
1) ret_texts 관련 부분.
2) 텍스트 임베딩을 마지막 토큰 기준으로 자르는 부분.

1)
retain text 부분에서 "for old_text, new_text in zip(ret_texts, ret_texts)" 이런 식으로 구현되어 있는데
이러면 "W = (W_old)[sum{(c_i^*)(c_i)^T}+lambda*(I)][sum((c_i)(c_i)^T)}+lambda*(I)]^(-1)"가 
	  "W = (W_old)[sum{(c_i)(c_i)^T}+lambda*(I)][sum((c_i)(c_i)^T)}+lambda*(I)]^(-1) = W_old"이 되어버리는 거 아닌가요?
따라서 업데이트가 일어나지 않을것 같은데...

2)
"Kelly Mckernan"을 "art"로 바꾸는 경우 "Kelly Mckernan"의 임베딩이 부적절하게 잘리는 것 아닌가요?
왜 마지막 토큰만 포함시키는지 모르겠습니다.


--- closed-from editing 문제점 ---
1) objective가 복잡해지면 closed-from solution을 찾는데 어려움이 생김.
2) 완전한 삭제를 보장하지 못함.
3) 모델 성능을 유지하는데 어려움을 보일 수 있음.
- 파라미터를 직접 변경하기 때문에 regularization이 충분하지 않거나 나머지 부분에서 변화를 예측하기 어려움.
4) 모델의 파라미터는 서로 연관되어 있기 때문에 모델의 특정 부분만 편집했을 때 부정적인 효과가 발생할 수 있음.
5) 모델마다 편집해야 하는 위치가 다를 수 있음.
- SD 모델은 cross-attention layer에 다양한 attribute 정보가 집중되어 있는 반면 그렇지 않은 모델도 있음.
- 정보가 다른 곳에 집중되어 있거나 아예 집중되어 있지 않은 경우 UCE는 확장성이 부족함.
6) interpretability를 떨어뜨릴 수 있음.
7) 미세 조정에 어려움이 생길 수 있음.