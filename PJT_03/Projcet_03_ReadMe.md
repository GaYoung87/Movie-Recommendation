# Projcet_03_ReadMe 

### 1.  상단에 고정시키며 다른 영역보다 우선하여 보기

```css
position: fixed;  /* sticky(고정하기)*/
top: 0;  /* 상단 -> if 오른쪽이면 right: 0; 하면 됨 */
z-index: 1000;  
/* 다른 영역보다 우선보게 수직 위치를 정함-> 값이 클수록 위에 놓여짐(=다른 것보다 위)*/
```



### 2. 정렬시키기

```css
float: right;  /* 정렬시키기 */
```



### 3. 세로 항목을 한 줄로 만들기

```css
display: inline-block;  /*  */
vertical-align: middle;  /*  */
```



### 4. 좌우 여백 지정하기

```css
margin: 0 7px;  /* 상하  좌우 나타냄으로 0(변화없음  7px만큼 좌우 여백) */
```



### 5. bullet point 제거

```css
list-style: none;
```



### 6. hover

```
마우스를 hover하는 곳에 가져다 두는 것으로 색상 변화 가능(color로)
```



### 7. text를 꾸며주는 밑줄 없애기

```css
text-decoration: none;
```



### 8. 배경 이미지 적용

```css
background-image: url("images/background.jpg");  /* url 가지고오기 */
background-size: cover;  /* cover에 맞추기 -> 아니면 확대되어 들어감 */
background-position: center;  /* 가운데에 맞추기 */
```



### 9. 텍스트 정렬

```css
text-align: center;  /* 가운데 정렬 */
line-height: 300px;  /* 수직 가운데 정렬 */
```



### 10. 폰트 사이즈 조정

```css
font-size: 2.5rem;
```



### 11. 패딩 제거

```css
padding: 0;
```



### 12.  부모 영역에 위치시키기

``` css
/* aside를 부모인 div#content의 영역에 위치시키세요.
div#content는 position: relative 입니다.
*/
position: absolute;  /* relative안쪽을 벗어나지 않음 */
top: 0;
```