// https://juni-official.tistory.com/141
function readJSON(file, callback) {
  var rawFile = new XMLHttpRequest();
  rawFile.overrideMimeType("application/json");
  rawFile.open("GET", file, true);
  rawFile.onreadystatechange = function() {
      if (rawFile.readyState === 4 && rawFile.status == "200") {
          callback(rawFile.responseText);
      }
  }
  rawFile.send(null);
}

readJSON("static/fruits.json", function(text){
  var fruit_data = JSON.parse(text);
  var json_length=Object.keys(fruit_data).length;
  //console.log(fruit_data[Object.keys(fruit_data)[0]]['img']);
  //console.log(fruit_data[Object.keys(fruit_data)[1]]['effect'].includes("Beauty Skin"));
  // tag 'Beauty skin'
  console.log(json_length);
  for(let i=0;i<json_length;i++){
    if(fruit_data[Object.keys(fruit_data)[i]]['color']=="Green"){
      var name=Object.keys(fruit_data)[i];
      const card_element = document.createElement('div');1
      card_element.className = 'item';
      const card_a = document.createElement('a');
      card_a.className = 'card';
      card_a.href='http://172.30.1.100:8080/detail?'+name;
      const card_div = document.createElement('div');
      card_div.className = 'thumb';
      var img_path = "url("+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
      console.log(img_path);
      card_div.style.backgroundImage="url("+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
      //card_div.style.backgroundImage="url(static/img/cabbage.png)";
      const card_article = document.createElement('article');
      card_article.className = 'item';
      const item_name = document.createElement('h1');
      item_name.className = 'card_name';
      item_name.innerText=name;
      const item_info = document.createElement('p');
      item_info.className = 'card_effect';
      card_element.appendChild(card_a);
      card_a.appendChild(card_div);
      card_a.appendChild(card_article);
      card_article.appendChild(item_info);
      card_article.appendChild(item_name);

      document.querySelector('.cardSpace').appendChild(card_element);

    };
  }
  // tag Promote Digestion
  for(let i=0;i<json_length;i++){
    if(fruit_data[Object.keys(fruit_data)[i]]['color']=="Red"){
      var name=Object.keys(fruit_data)[i];
      const card_element = document.createElement('div');
      card_element.className = 'item';
      const card_a = document.createElement('a');
      card_a.className = 'card';
      card_a.href='http://172.30.1.100:8080/detail?'+name;
      const card_div = document.createElement('div');
      card_div.className = 'thumb';
      var img_path = "url(img/"+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
      console.log(img_path);
      card_div.style.backgroundImage="url("+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
      //card_div.style.backgroundImage="url(static/img/cabbage.png)";
      const card_article = document.createElement('article');
      card_article.className = 'item';
      const item_name = document.createElement('h1');
      item_name.className = 'card_name';
      item_name.innerText=name;
      const item_info = document.createElement('p');
      item_info.className = 'card_effect';
      card_element.appendChild(card_a);
      card_a.appendChild(card_div);
      card_a.appendChild(card_article);
      card_article.appendChild(item_info);
      card_article.appendChild(item_name);
      document.querySelector('.cardSpace2').appendChild(card_element);
    };
  }
  // tag Osteporosis Prevention
  for(let i=0;i<json_length;i++){
    if(fruit_data[Object.keys(fruit_data)[i]]['color']=="White"){
      var name=Object.keys(fruit_data)[i];
      console.log(i);
      const card_element = document.createElement('div');
      card_element.className = 'item';
      const card_a = document.createElement('a');
      card_a.className = 'card';
      card_a.href='http://172.30.1.100:8080/detail?'+name;
      const card_div = document.createElement('div');
      card_div.className = 'thumb';
      var img_path = "url(img/"+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
      console.log(img_path);
      card_div.style.backgroundImage="url("+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
      //card_div.style.backgroundImage="url(static/img/cabbage.png)";
      const card_article = document.createElement('article');
      card_article.className = 'item';
      const item_name = document.createElement('h1');
      item_name.className = 'card_name';
      item_name.innerText=name;
      const item_info = document.createElement('p');
      item_info.className = 'card_effect';
      card_element.appendChild(card_a);
      card_a.appendChild(card_div);
      card_a.appendChild(card_article);
      card_article.appendChild(item_info);
      card_article.appendChild(item_name);
      document.querySelector('.cardSpace3').appendChild(card_element);
    };
  }
  // tag Hypertension Prevention
  for(let i=0;i<json_length;i++){
    if(fruit_data[Object.keys(fruit_data)[i]]['color']=="Orange"){
      var name=Object.keys(fruit_data)[i];
      console.log(i);
      const card_element = document.createElement('div');
      card_element.className = 'item';
      const card_a = document.createElement('a');
      card_a.className = 'card';
      card_a.href='http://172.30.1.100:8080/detail?'+name;
      const card_div = document.createElement('div');
      card_div.className = 'thumb';
      var img_path = "url("+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
      console.log(img_path);
      card_div.style.backgroundImage="url("+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
      //card_div.style.backgroundImage="url(static/img/cabbage.png)";
      const card_article = document.createElement('article');
      card_article.className = 'item';
      const item_name = document.createElement('h1');
      item_name.className = 'card_name';
      item_name.innerText=name;
      const item_info = document.createElement('p');
      item_info.className = 'card_effect';
      card_element.appendChild(card_a);
      card_a.appendChild(card_div);
      card_a.appendChild(card_article);
      card_article.appendChild(item_info);
      card_article.appendChild(item_name);
      document.querySelector('.cardSpace4').appendChild(card_element);
    };
  } 
  

});