# 파이썬에서 함수를 호출할 때 매개변수의 이름을 명시하여 값을 전달하는 방식
# 매개변수 순서에 상관없이 값을 전달할 수 있고, 코드의 가독성과 명확성을 높임

@app.get("/items/{id}", response_class=HTMLResponse)    # response_class라는 파라미터에 HTMLResponse라는 값을 명시적으로 전달
