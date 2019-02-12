var myList = document.getElementById('myList');
var myInput = document.getElementById('myInput');
var myClicker = document.getElementById('submit');
var onSubClick = function(e)
{
    if(myInput.value !== "")
    {
        var newLi = document.createElement('li');
        var newCheck = document.createElement('input');
        var newSpan = document.createElement('span');
        var newImg = document.createElement('img');
        var newP = document.createElement('p');
        newImg.className = "myImage";
        newImg.src = "musor.jpg";
        newCheck.type = "checkbox";
        newCheck.className = "myCheck";
        newSpan.className = "mySpan";
        newP.innerHTML = myInput.value;
        newCheck.onclick = onLiClick;
        newImg.onclick = deletAll;
        newSpan.appendChild(newCheck);
        newSpan.appendChild(newP);
        newLi.appendChild(newSpan);
        newLi.appendChild(newImg);
        myList.appendChild(newLi);
        myInput.value = "";
        
    }
    else{
        alert("Input is UNDEFINED!!!");
    }
};

var onLiClick = function(e)
{
    if(e.target.checked)
    {
        var cur = e.target.parentNode;
        cur.className = "newDivClass";
    }
    else{
        var cur = e.target.parentNode;
        cur.className = "mySpan";
    }
    console.log(e.target);
   
};
 
var deletAll  = function(e)
{
    var bigLi = event.target.parentNode;
    bigLi.remove();
}

