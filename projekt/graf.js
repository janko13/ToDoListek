var ctx;
var canvas;
var sredinaX;
var sredinaY;
var dolzinaX;
var dolzinaY;

var ucin = [60, 40, 100, 80];
var aktiv = [3, 4, 5, 8];
var stanje = 0;

function start(){
	canvas = document.getElementById("myCanvas");
	ctx = canvas.getContext("2d");
	onWindowResize();
	
	window.addEventListener('resize', onWindowResize, false);
	
	document.getElementById('Aktivnosti').onclick = function () {
		stanje = 1;
        aktivnosti();
    };
	
	document.getElementById('Ucinkovitost').onclick = function () {
		stanje = 2;
        ucinkovitost();
    };

}

function onWindowResize() {

	canvas.width = window.innerWidth*3/4;
	canvas.height = window.innerHeight/2;
	sredinaX = canvas.width/2;
    sredinaY = canvas.height/2;
	dolzinaX = canvas.width;
    dolzinaY = canvas.height;
	
	if(stanje==0){
		narisiOgrodje();
	}
	if(stanje==1){
		aktivnosti();
	}
	else{
		ucinkovitost();
	}
	
}


function narisiOgrodje(){
	ctx.strokeStyle="black";
	ctx.lineWidth=2;
	ctx.moveTo(dolzinaX/10, dolzinaY/10);
	ctx.lineTo(dolzinaX/10, dolzinaY*9/10);
	ctx.lineTo(dolzinaX*9/10, dolzinaY*9/10);
	ctx.stroke();
	
	ctx.lineWidth=1;
	ctx.moveTo(dolzinaX/10, dolzinaY*3/10);
	ctx.lineTo(dolzinaX*9/10, dolzinaY*3/10);
	ctx.moveTo(dolzinaX/10, dolzinaY*5/10);
	ctx.lineTo(dolzinaX*9/10, dolzinaY*5/10);
	ctx.moveTo(dolzinaX/10, dolzinaY*7/10);
	ctx.lineTo(dolzinaX*9/10, dolzinaY*7/10);
	ctx.stroke();
	
}

function aktivnosti(){
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	narisiOgrodje();
	ctx.lineWidth="2";
	ctx.strokeStyle="red";
	
	var enotaX = (dolzinaX*8/10)/(aktiv.length*2+1);
	var enotaY = dolzinaY/10;
	var enotaYY = enotaY*8/10;
	
	for (i = 0; i < aktiv.length; i++) { 
		ctx.beginPath();
		ctx.rect((2*i+2)*enotaX,enotaY+(10-aktiv[i])*enotaYY,enotaX,aktiv[i]*enotaYY);
		ctx.stroke()
	}
}

function ucinkovitost(){
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	narisiOgrodje();
	ctx.lineWidth="2";
	ctx.strokeStyle="blue";
	
	var enotaX = (dolzinaX*8/10)/(ucin.length*2+1);
	var enotaY = dolzinaY/10;
	var enotaYY = enotaY*8/100;
	
	for (i = 0; i < ucin.length; i++) {
		
		ctx.beginPath();
		ctx.rect((2*i+2)*enotaX,enotaY+(100-ucin[i])*enotaYY,enotaX,ucin[i]*enotaYY);
		ctx.stroke();
	}
}