(function(){
        document.getElementById("submit").onclick =
        function validateForm() {
            var x = document.forms["form"]["wage"].value;
            var y = document.forms["form"]["hours"].value;
            var z = document.forms["form"]["holiday"].value;
            if (x=="" || y=="" || z=="") {
                //document.forms["form"]["wage"].value = 0;
                alert("Please, fill out all fields to properly calculate your paycheck!");
                return false;
            }
        }
    
})();