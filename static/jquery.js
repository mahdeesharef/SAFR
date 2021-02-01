$(function () {

   "use strict";
  
   $(document).ready(function(){
  
    
     $(".header .container .notification .box .open").click(function(){
         $(".header .container .notification .ul-2").slideDown(1000);
         $(".header .container .box-para").css("display","none");
         $(".header .container .box .container .big-box").css("display","none");
        
         $(".header .container .notification .box .close").css("display","flex");
         $(".header .container .notification .box .open").css("display","none");
         
     });
       
      
     $(".header .container .notification .box .close").click(function(){
         $(".header .container .notification .ul-2").slideUp(1000);
         $(".header .container .box-para").fadeIn(1500).css("display","flex");
         $(".header .container .box .container .big-box").fadeIn(1500).css("display","block");
         $(".header .container .notification .box .close").css("display","none");
         $(".header .container .notification .box .open").css("display","flex");
         
     });
   

 

   });
});
  