document.addEventListener("DOMContentLoaded", function () {
    //this is where to input the java script code
   document.getElementById("sign_up").
    addEventListener("click",function() {
     const username=
         document.getElementById("User-Name").value;
        
          const email=  document.getElementById("Email").value;
         
        const password=
        document.getElementById("Password").value;

         // Simple validation
         if (username===""||email ===""||password===""){
            alert(" Please fill in all fields");
        return;}
         else { alert("sign up Successful!")}
         
            //redirect to homepage
            window.open("/template/dash.html","_blank")

            //saving user credentials for login purposes
            const user={
                username,
                email,
                password
            };

            localStorage.setItem("user",JSON.stringify(user));
            console.log("user")

    })
});


    