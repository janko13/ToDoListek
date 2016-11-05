var ctx;
var canvas;
var sredinaX;
var sredinaY;

function start(){
	canvas = document.getElementById("myCanvas");
	canvas.width = window.innerWidth/2;
	canvas.height = window.innerHeight/2;
    ctx = canvas.getContext("2d");
	sredinaX = canvas.width / 2;
    sredinaY = canvas.height / 2;
	ctx.moveTo(0, 0);
    ctx.lineTo(sredinaX, sredinaY);
	ctx.lineTo(sredinaX, sredinaY*2);
	ctx.stroke();
}