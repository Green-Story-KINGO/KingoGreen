// https://juni-official.tistory.com/141
// for read json file
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

// read fruit json file
readJSON("static/fruits.json", function(text){
  var fruit_data = JSON.parse(text);
  var json_length=Object.keys(fruit_data).length;
  // sort by Green color
  for(let i=0;i<json_length;i++){
    // initialize each fruit(or vegetable) card
    if(fruit_data[Object.keys(fruit_data)[i]]['color']=="Green"){
      var name=Object.keys(fruit_data)[i];
      const card_element = document.createElement('div');
      card_element.className = 'item';
      const card_a = document.createElement('a');
      card_a.className = 'card';
      card_a.href='http://127.0.0.1:8080/detail?'+name;
      const card_div = document.createElement('div');
      card_div.className = 'thumb';
      var img_path = "url("+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
      card_div.style.backgroundImage="url("+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
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
      // add card element into space of 'green'
      document.querySelector('.cardSpace').appendChild(card_element);

    };
  }
  // sort by red color
  for(let i=0;i<json_length;i++){
    // initialize each fruit(or vegetable) card
    if(fruit_data[Object.keys(fruit_data)[i]]['color']=="Red"){
      var name=Object.keys(fruit_data)[i];
      const card_element = document.createElement('div');
      card_element.className = 'item';
      const card_a = document.createElement('a');
      card_a.className = 'card';
      card_a.href='http://127.0.0.1:8080/detail?'+name;
      const card_div = document.createElement('div');
      card_div.className = 'thumb';
      var img_path = "url(img/"+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
      console.log(img_path);
      card_div.style.backgroundImage="url("+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
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
      // add card element into space of 'red'
      document.querySelector('.cardSpace2').appendChild(card_element);
    };
  }
  // sort by white color
  for(let i=0;i<json_length;i++){
    // initialize each fruit(or vegetable) card
    if(fruit_data[Object.keys(fruit_data)[i]]['color']=="White"){
      var name=Object.keys(fruit_data)[i];
      const card_element = document.createElement('div');
      card_element.className = 'item';
      const card_a = document.createElement('a');
      card_a.className = 'card';
      card_a.href='http://127.0.0.1:8080/detail?'+name;
      const card_div = document.createElement('div');
      card_div.className = 'thumb';
      var img_path = "url(img/"+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
      console.log(img_path);
      card_div.style.backgroundImage="url("+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
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
       // add card element into space of 'white'
      document.querySelector('.cardSpace3').appendChild(card_element);
    };
  }
  // sort by orange color
  for(let i=0;i<json_length;i++){
    // initialize each fruit(or vegetable) card
    if(fruit_data[Object.keys(fruit_data)[i]]['color']=="Orange"){
      var name=Object.keys(fruit_data)[i];
      console.log(i);
      const card_element = document.createElement('div');
      card_element.className = 'item';
      const card_a = document.createElement('a');
      card_a.className = 'card';
      card_a.href='http://127.0.0.1:8080/detail?'+name;
      const card_div = document.createElement('div');
      card_div.className = 'thumb';
      var img_path = "url("+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
      card_div.style.backgroundImage="url("+fruit_data[Object.keys(fruit_data)[i]]['img']+")";
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
      // add card element into space of 'orange'
      document.querySelector('.cardSpace4').appendChild(card_element);
    };
  } 
  

});