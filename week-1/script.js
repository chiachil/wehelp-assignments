// XMLHttpRequest方法
// var requestURL = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json';//用變數存網址
// var request = new XMLHttpRequest(); //建立請求
// request.open('GET', requestURL); //開啟請求
// request.responseType = 'json'; //回傳json格式
// request.send(); //送出請求
// request.onload = function() { //只要成功回傳響應，就會觸發載入事件，會執行以下事件處理器
//     var data = request.response.result.results; //用變數存回應
//     showAttrList(data); //呼叫顯示圖片函式
// }
// function showAttrList(data) {
//   for(i = 0; i < 8; i++) {
//     var attrList = document.createElement('li');
//     var attrPic = document.createElement('img');
//     var attrName = document.createElement('span');
//     attrList.classList.add("item", "mb-16");
//     attrPic.src = "https://"+data[i].file.split("https://")[1];
//     attrName.textContent = data[i].stitle;
//     attrList.appendChild(attrPic);
//     attrList.appendChild(attrName);
//     var listContainer = document.getElementById("listContainer");
//     listContainer.appendChild(attrList);
//     };
//   }
//fetch方法
let url ="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
fetch(url, {method: 'GET'})
.then(function(response) { //fetch後回應的是readableStream物件
    return response.json(); //轉換成json，再傳入下一個then
  })
.then(function(jsonData) { //用程式執行我們要的資料
    let data = jsonData.result.results;
    for(i = 0; i < 8; i++) {
        var attrList = document.createElement('li'); //新增li標籤
        var attrPic = document.createElement('img'); //新增img標籤
        var attrName = document.createElement('span'); //新增span標籤
        attrList.classList.add("item"); //加上li的class屬性
        attrPic.src = "https://"+data[i].file.split("https://")[1]; //加上img的來源
        attrName.textContent = data[i].stitle; //加上span內文字
        attrList.appendChild(attrPic); //li內放img
        attrList.appendChild(attrName); //li內放span
        var listContainer = document.getElementById("listContainer"); //取ul標籤
        listContainer.appendChild(attrList);//ul內放li
    };
  });