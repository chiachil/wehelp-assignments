function getData(){
  let username = document.getElementById("username")
  let apiUrl = "http://127.0.0.1:3000/api/members?username=" + username.value;
  let req = new XMLHttpRequest;
  req.open("GET", apiUrl, true);
  req.onload = function(){
    let data = JSON.parse(this.responseText); //JSON字串轉換成JS物件
    let result = data.data;
    if (result == null){
      let content = "無此會員";
      document.getElementById("content").innerHTML = content;
    } else {
      let content = result.name + "（" + result.username + "）";
      document.getElementById("content").innerHTML = content;
    }
  };
  req.send();
}