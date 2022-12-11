let counter = 0
let gender = 0;
let UserFirstName = ''
let UserLastName = ''
let UserGender = 0
let UserEmail = ''
let UserPassword = ''
let correct = 0
let loginCorrect = 0

function passwordCheck(str) { // Here this function checks to see if th password has correct format
    // Regex to check if a string
    // contains uppercase, lowercase
    // special character & numeric value
    let pattern = new RegExp( // https://bobbyhadz.com/blog/javascript-check-if-string-contains-character
      "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[-+_!@#$%^&*.,?]).+$" // This is where we check if there are any special characters in
    );

    // If the string is empty
    // then print No
    if (!str || str.length === 0) {
      return 0;
    }

    // Print Yes If the string matches
    // with the Regex
    if (pattern.test(str)) {
        return 1
    } else {
        return 0
    }
  }

  function firstLetterCap(str) { // This checks to see if the first character is a capital letter
    if(str[0].toUpperCase() === str[0]){ // https://bobbyhadz.com/blog/javascript-check-if-string-contains-character
        return 1
    }
    return 0
  }

  function containNumber(str) { // This checks to see if the irst letter is a capital letter
    if (/[0-9]/.test(str)) { // https://bobbyhadz.com/blog/javascript-check-if-string-contains-character
        return 0
    }
    return 1
  }

  function specialCharacterCheck(str){ // This checks to see if there are any special characters
    if(/^[a-zA-Z0-9 ]*$/.test(str)) { // https://bobbyhadz.com/blog/javascript-check-if-string-contains-character
        return 1;
    }
    return 0
  }
 
$('.loginPage').click(function() { // This loads the login page

    $('.container').fadeOut(0);
    $('.container').fadeIn(1000)
    
    if(counter ==0 ) {
      $(".topPage").empty();
      $(".info").empty();
      $(".buttonPlace").empty();
    }

    if (counter> 0) {
        $(".topPage").empty(); // This checks to see if the page has already been visited
        $(".info").empty();
        $(".buttonPlace").empty();

    }
    counter++; // This indicates the page has been visited
    $('.loginPage').prop('disabled', true) // This disables the other tab
    $('.signPage').prop('disabled', false)


    $('.container').css({height: '350px'});

    let loginHead = $('<h2></h2>').text("Login")

    loginHead.css({color:'black'});

    let loginInfo = $('<a></a>').text("Enter user name and password:")
    loginInfo.css({'color': 'black', 'margin-bottom' :'7px'})

    $('.topPage').append(loginHead)
    $('.topPage').append(loginInfo)


    // This is where we put the login info

    let email = $('<p></p>').text("Username")
    email.css({'color': 'black', 'font-size': '10pt' , 'width': '100%','margin-bottom' :'3px', 'margin-top': '8px' })
    let emailBox = $('<input type=text></input>')
    emailBox.attr('placeholder', 'Username')
    emailBox.css({'color': ' #384047', 'background-color': 'whitesmoke' , 'border': '1px solid black', 'width': '100%', 'margin-bottom' :'10px'})

    $('.info').append(email)
    $('.info').append(emailBox)

    let password = $('<p></p>').text("Password")
    password.css({'color': 'black', 'font-size': '10pt', 'width': '100%','margin-bottom' :'3px' })
    let passwordBox = $('<input type=password></input>')
    passwordBox.attr('placeholder', 'Password')
    passwordBox.css({'color': ' #384047', 'background-color': 'whitesmoke' , 'border': '1px solid black', 'width': '100%', 'margin-bottom' :'10px'})

    $('.info').append(password)
    $('.info').append(passwordBox)

    let loginButton = $('<button></button>')
    loginButton.text("Login")
    loginButton.css({ 'text-align':'center', 'color':'white', 'width': '100%', 'height': '40px','background-color': 'green', 'font-weight':'bold', 'border-width':"0px", 
    'border-radius':"3px"
  })

    $('.buttonPlace').append(loginButton)
    loginButton.click(function(){
        console.log(emailBox.val())
        console.log(passwordBox.val())
        console.log(UserEmail)
        console.log(UserPassword)
        if(emailBox.val().length > 0 && passwordBox.val().length > 0){
          console.log("in")
            temp = true
            //if(emailBox.val() == UserEmail && passwordBox.val() == UserPassword){ // Validates the email and password
            if(temp){ // Validates the email and password
                $.ajax({
                  type:'POST',
                  url:'http://172.30.1.100:8080/updateuser',
                  data:{
                    "user_name": emailBox.val(),
                    "pw": passwordBox.val(),
                  },
                  dataType: 'json',
        
                  success:function(data)
                  {
                    cur_name = data['user_name'];
                    window.localStorage.setItem('curUser', cur_name);
                    console.log(data['success']);
                    console.log(typeof(data['success']));
                    if(data['success']==1){
                      $('.container').css({height: '100px'});
                      $(".topPage").empty();
                      $(".info").empty();
                      $(".buttonPlace").empty();
                      let loginHead = $('<h2></h2>').text("You are logged in.")
                      loginHead.css({color:'black'});
                      $('.topPage').append(loginHead)
                      alert("Login Success!");
                      location.replace("http://172.30.1.100:8080/home")
                    }
                    else{
                      alert("Login Failed!");
                      loginInfo.text("Credentials do not match!")
                      loginInfo.css('color', 'red')
                    }
                      
                  },
        
                  error: function() {
                      alert('error');
                  }
                });
            }
            else {
                


            }
        }
        






    })


    //Now we are going to create functions to check conditions
    let emailValue = emailBox.val()
    console.log(typeof emailValue)
    console.log(emailValue.length)

      

})


let alarm = "";
let empty = 0;
let emailEmpty = 0

function ValidateEmail(email)
{
    let emailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if(email.match(emailformat))
      {
        return true;
      }
    else
      {
        return false;
      }
}

$('.signPage').click(function() { // This brings us to the sign up page
  $('.container').fadeOut(0);
  $('.container').fadeIn(1000) // This fades in and fades out the page

  if( counter == 0) {
    $(".topPage").empty();
    $(".info").empty();
    $(".buttonPlace").empty();
  }
    if (counter > 0) {
        $(".topPage").empty();
        $(".info").empty();
        $(".buttonPlace").empty();

    }
    counter++;
    let clicked = 0

    $('.loginPage').prop('disabled', false)
    $('.signPage').prop('disabled', true)
    

    $('.container').css({height: '450px'});

    let signHead = $('<h2></h2>').text("Sign up")

    signHead.css({color:'black'});

    let signInfo = $('<a></a>').text("Fill in the form:")
    signInfo.css('color', 'black')

    $('.topPage').append(signHead)
    $('.topPage').append(signInfo)


    // This is where we put the login info
    let firstName = $('<p></p>').text("Username")
    firstName.css({ 'color': 'black', 'font-size': '10pt' , 'width': '100%', 'margin-bottom' :'3px', 'margin-top' :' 8px'})
    let firstBox = $('<input type=text></input>')
    firstBox.attr('placeholder', 'Username')
    firstBox.css({'margin-bottom' :'10px','color': ' #384047', 'background-color': 'whitesmoke' , 'border': '1px solid black', 'width': '100%'})

    
    $('.info').append(firstName)
    $('.info').append(firstBox)
    
     

    let email = $('<p></p>').text("Email")
    email.css({'color': 'black', 'font-size': '10pt' , 'width': '100%', 'margin-bottom' :'3px'})
    let emailBox = $('<input type=text></input>')
    emailBox.attr('placeholder', 'Email')
    emailBox.css({'margin-bottom' :'10px','color': ' #384047', 'background-color': 'whitesmoke' , 'border': '1px solid black', 'width': '100%'})


    $('.info').append(email)
    $('.info').append(emailBox)



    let password = $('<p></p>').text("Password")
    password.css({'color': 'black', 'font-size': '10pt', 'width': '100%', 'margin-bottom' :'3px' })
    let passwordBox = $('<input type=password></input>')
    passwordBox.attr('placeholder', 'Password')
    passwordBox.css({ 'margin-bottom' :'10px','color': ' #384047', 'background-color': 'whitesmoke' , 'border': '1px solid black', 'width': '100%', 'margin-bottom' :'10px'})

    $('.info').append(password)
    $('.info').append(passwordBox)
    
    let confPassword = $('<p></p>').text("Confirm Password")
    confPassword.css({'color': 'black', 'font-size': '10pt', 'width': '100%', 'margin-bottom' :'3px' })
    let confBox = $('<input type=password></input>')
    confBox.attr('placeholder', 'Confirm Password')
    confBox.css({'margin-bottom' :'10px', 'color': ' #384047', 'background-color': 'whitesmoke' , 'border': '1px solid black', 'width': '100%', 'margin-bottom' :'10px'})
   
  
    $('.info').append(confPassword)
    $('.info').append(confBox)


    let SignButton = $('<button></button>')
    SignButton.text("Sign Up")
    SignButton.css({'background-color':'green', 'text-align':'center', 'color':'white', 'width': '100%', 'height': '40px', 'font-weight':'bold', 'border-width':"0px", 
    'border-radius':"3px"})

    $('.buttonPlace').append(SignButton)

    let emailCheck = 0
    let passwordCheck = 0
    SignButton.click(function(){ // This is the sign up  button

        
      if(firstBox.val().length === 0){ 
        firstBox.css('border', '1px solid red')
        empty++;
              
              
      

        alarm +="\nPlease enter your username"
        console.log(alarm)
      }
      else {
        firstBox.css('border', '1px solid black')

      }

      if(emailBox.val().length === 0){
        emailBox.css('border', '1px solid red')
        empty++;
        emailEmpty++;
              
              
      

        alarm += "\nPlease enter your email"
        console.log(alarm)

      }

      
      if(passwordBox.val().length === 0){
        passwordBox.css('border', '1px solid red')
        empty++;
              
              
  
        alarm += "\nPlease enter your password"
        console.log(alarm)


      }
      else {
        passwordBox.css('border', '1px solid black')

      }
      if(confBox.val().length === 0){
        confBox.css('border', '1px solid red')
        empty++;

      }
      else {
        confBox.css('border', '1px solid black')

      }

      if(empty > 0 && emailEmpty > 0) {
        alert(alarm)
        console.log(alarm)
      }

      else if(empty == 0 && emailEmpty == 0) {
        if (!ValidateEmail(emailBox.val())){
          emailBox.css({'margin-bottom' :'10px','color': ' #384047', 'background-color': 'whitesmoke' , 'border': '1px solid red', 'width': '100%'})
          alert("You have entered an invalid email address!");
    
        }
        else {
          emailCheck++;
          emailBox.css({'margin-bottom' :'10px','color': ' #384047', 'background-color': 'whitesmoke' , 'border': '1px solid black', 'width': '100%'})
    
        }
      }

      if(confBox.val() == passwordBox.val()){
        confBox.css({'margin-bottom' :'10px', 'color': ' #384047', 'background-color': 'whitesmoke' , 'border': '1px solid black', 'width': '100%', 'margin-bottom' :'10px'})
  
        passwordCheck++;
      }
      else {
        confBox.css({'margin-bottom' :'10px', 'color': ' #384047', 'background-color': 'whitesmoke' , 'border': '1px solid red', 'width': '100%', 'margin-bottom' :'10px'})
      }

        if(passwordCheck == 1 && emailCheck == 1){ // If enough correct happened then we sign in
          // If the email format and confirm password matches password
        $('.container').css({height: '200px'});

      
            $(".topPage").empty();
            $(".info").empty();
            $(".buttonPlace").empty();

            let signHead = $('<h2></h2>').text("You are signed up.")
    
            signHead.css({color:'black'});
            $('.topPage').append(signHead);
            
            $.ajax({
              type:'POST',
              url:'http://172.30.1.100:8080/makeid',
              data:{
                "username": firstBox.val(),
                "email": emailBox.val(),
                "pw": passwordBox.val(),
                "cfpw": confBox.val()
              },
              dataType: 'json',
    
              success:function(data)
              {
                  alert('Success');
              },
    
              error: function() {
                  alert('error');
              }
            });
    
        }
     

        empty = 0
        correct = 0
        alarm = " "
        emailEmpty = 0
        emailCheck = 0
        passwordCheck = 0

    })




    // Now we are going to check the conditions of each

})


// $(document.body).delegate('.buy_class', 'click', function() {





// }



