function includeHTML() {
  var z, i, elmnt, file, xhttp;
  /* Loop through a collection of all HTML elements: */
  z = document.getElementsByTagName("*");
  for (i = 0; i < z.length; i++) {
    elmnt = z[i];
    /*search for elements with a certain atrribute:*/
    file = elmnt.getAttribute("w3-include-html");
    if (file) {
      /* Make an HTTP request using the attribute value as the file name: */
      xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function () {
        if (this.readyState == 4) {
          if (this.status == 200) {
            elmnt.innerHTML = this.responseText;
          }
          if (this.status == 404) {
            elmnt.innerHTML = "Page not found.";
          }
          /* Remove the attribute, and call this function once more: */
          elmnt.removeAttribute("w3-include-html");
          includeHTML();
        }
      };
      xhttp.open("GET", file, true);
      xhttp.send();
      /* Exit the function: */
      return;
    }
  }
}

// Phát hiện hướng cuộn cho logo


// Cho phần liên hệ

function showname(i) {
  var p = document.getElementById("contact__desc");
  p.innerHTML = i;
}

function hidename() {
  var p = document.getElementById("contact__desc");
  p.innerHTML = "Hover or click in avatar";
}

//

function back() {
  window.history.back();
}


window.onscroll = function (f) {
  var navs = document.getElementsByClassName("nav");

  if (window.pageYOffset <= 100) {
    var navs = document.querySelector("nav");
    navs.classList.add("transpr");
  } else {
    navs = document.querySelector("nav");
    navs.classList.remove("transpr");
  }
  var logo = document.getElementById("logo__disappear");

  if (this.oldScroll < this.scrollY) {
    logo.style.marginRight = "-6rem";
    logo.style.opacity = "0";
  } else {
    logo.style.marginRight = "0";
    logo.style.opacity = "1";
  }

  this.oldScroll = this.scrollY;
};
