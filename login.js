//1. id,pw에 각각 한 글자 이상 써야 버튼이 활성화 되도록 해주세요.
//2. 원래 연한 파란색이었다가 -> 활성화 되면 파란색으로!

const id = document.getElementsByClassName('id');
const idValue = document.getElementsByClassName('id').value;
const pw = document.getElementsByClassName('password').value;
const bt = document.getElementsByTagName('button');

id.addEventListener('keypress',function(e) {
    // console.log(e)
    console.log(id.value)
    if (id.length && pw.length >= 1) {
        bt.background = blue;
    } 
});
