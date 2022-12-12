function changeSliderImage(e) {
  let findElementActive = document.getElementsByClassName("thumbnail active");
  let findBackgroundImageElement = document.getElementsByClassName(
    "auth-container"
  );
  findElementActive[0].classList.remove("active");
  let imgElement = e.querySelector("img");
  findBackgroundImageElement[0].style.backgroundImage = `url('${imgElement.src.replace(
    "th-",
    ""
  )}')`;
  e.classList.remove("active");
  e.classList.add("active");
}
