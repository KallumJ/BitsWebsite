const masterpageStyle = `background: url("$") no-repeat center center fixed; -webkit-background-size: cover; -moz-background-size: cover; -o-background-size: cover; background-size: cover;`
const imageDir = "../static/assets/images/downloads/"

// Preload images, so theres no white flash
let wd1Img = new Image()
wd1Img.src = imageDir + "112.png"

let wd2Img = new Image()
wd2Img.src = imageDir + "113.png"

let wd3Img = new Image()
wd3Img.src = imageDir + "114.png"

let vResourceImg = new Image()
vResourceImg.src = imageDir + "vanillapack.jpg"

let bResourceImg = new Image()
bResourceImg.src = imageDir + "bitsplus.png"

let initalBackgroundImg = new Image()
initalBackgroundImg.src = imageDir + "DownloadsBackground.png"


// Store images in array so JS doesnt release them
let images = [wd1Img, wd2Img, wd3Img, vResourceImg, bResourceImg, initalBackgroundImg]

function changeImg(index) {
    document.getElementById("masterpage").style = masterpageStyle.replace("$", images[index].src)
}

function resetImg() {
    changeImg(5)
}

function wd1On() {
    changeImg(0);
}

function wd1Off() {
    resetImg()
}

function wd1Redirect() {
    location.href = "https://hogwarts.bits.team/world-download/1.12"
}

function wd2On() {
    changeImg(1)
}

function wd2Off() {
    resetImg()
}

function wd2Redirect() {
    location.href = "https://hogwarts.bits.team/world-download/1.13"
}

function wd3On() {
    changeImg(2)
}

function wd3Off() {
    resetImg()
}

function wd3Redirect() {
    location.href = "http://hogwarts.bits.team/world-download/1.15"
}

function vResourceOn() {
    changeImg(3)
}

function vResourceOff() {
    resetImg()
}

function vResourceRedirect() {
    location.href = "https://bits.team/resourcepack"
}

function bResourceOn() {
    changeImg(4)
}

function bResourceOff() {
    resetImg()
}

function bResourceRedirect() {
    location.href = "https://hogwarts.bits.team/resources"
}
