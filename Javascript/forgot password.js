document.addEventListener("DOMContentLoaded", function () {

    const Forget= document.getElementById("Forget-Password");

    Forget.addEventListener("click",function(){
        const email=document.getElementById("email").value;

        //const password=document.getElementById("password").value;

        const savedUser=JSON.parse(localStorage.getItem("user"));

        if (!savedUser){ alert("No User found.Please Sign up");
            return;
        }

        if (email=== savedUser.email)
        {alert ("Login Succesfuls");
            window.open("dash.chat.html","_blank");
        }  else { alert(" Wrong Email or Password")}

    })

});
