// <!---------------- js for responsive navbar -------------------->
    const menuBtn = document.querySelector(".menu-icon span");
    const searchBtn = document.querySelector(".search-icon");
    const cancelBtn = document.querySelector(".cancel-icon");
    const items = document.querySelector(".nav-items");
    const form = document.querySelector("form");
    menuBtn.onclick = () => {
        items.classList.add("active");
        menuBtn.classList.add("hide");
        searchBtn.classList.add("hide");
        cancelBtn.classList.add("show");
    }
    cancelBtn.onclick = () => {
        items.classList.remove("active");
        menuBtn.classList.remove("hide");
        searchBtn.classList.remove("hide");
        cancelBtn.classList.remove("show");
        form.classList.remove("active")
        cancelBtn.style.color = "#ff3d00";

    }
    searchBtn.onclick = () => {
        form.classList.add("active")
        searchBtn.classList.add("hide");
        cancelBtn.classList.add("show");
    }
//---------------- end of js for responsive navbar -------------------->


// ---------------- js for image gallary --------------------

    var productImg = document.getElementById("productImg");
    var smallImg = document.getElementsByClassName("small-img");

    smallImg[0].onclick = function () {
        productImg.src = smallImg[0].src;
    }
    smallImg[1].onclick = function () {
        productImg.src = smallImg[1].src;
    }
    smallImg[2].onclick = function () {
        productImg.src = smallImg[2].src;
    }
    smallImg[3].onclick = function () {
        productImg.src = smallImg[3].src;
    }
// ----------------  end of js for image gallary --------------------






    



