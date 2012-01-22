var menuSlider=function(){
	var m,e,g,s,q,i; e=[]; q=8; i=8;
	return{
		init:function(j,k){
			m=document.getElementById(j); e=m.getElementsByTagName('li');
			var i,l,w,p; i=0; l=e.length;
			for(i;i<l;i++){
				var c,v; c=e[i]; v=c.value; if(v==1){s=c; w=c.offsetWidth; p=c.offsetLeft}
				c.onmouseover=function(){menuSlider.mo(this)}; c.onmouseout=function(){menuSlider.mo(s)};
			}
			g=document.getElementById(k); g.style.width=w+'px'; g.style.left=p+'px';
		},
		mo:function(d){
			clearInterval(m.tm);
			var el,ew; el=parseInt(d.offsetLeft); ew=parseInt(d.offsetWidth);
			m.tm=setInterval(function(){menuSlider.mv(el,ew)},i);
		},
		mv:function(el,ew){
			var l,w; l=parseInt(g.offsetLeft); w=parseInt(g.offsetWidth);
			if(l!=el||w!=ew){
				if(l!=el){var ld,lr,li; ld=(l>el)?-1:1; lr=Math.abs(el-l); li=(lr<q)?ld*lr:ld*q; g.style.left=(l+li)+'px'}
				if(w!=ew){var wd,wr,wi; wd=(w>ew)?-1:1; wr=Math.abs(ew-w); wi=(wr<q)?wd*wr:wd*q; g.style.width=(w+wi)+'px'}
			}else{clearInterval(m.tm)}
}};}();


function lookup(inputString) {
	$('#search').css('visibility:hidden');
	if(inputString.length == 0) {
		// Hide the suggestion box.
		$('#suggestions').hide();
	} else {
		// post data to our php processing page and if there is a return greater than zero
		// show the suggestions box
		$.post('cityname/', {mysearchString: ""+inputString+""}, function(data){
			if(data.length >0) {
				$('#suggestions').show();
				$('#autoSuggestionsList').html(data);
			}
		});
	}
} //end

// if user clicks a suggestion, fill the text box.
function fill(thisValue) {
	$('#suggestions').slideUp(500,load(thisValue));
	
}
function load(thisValue){
		$('#inputString').val(thisValue);
		$.post('get_by_cityname/', { mysearchString: ""+thisValue+""}, function(data){
			
			if(data.length >0) {
				$('#search').css('visibility','visible').html(data);
				
			}
			
		});
}

function getmovie(d,thisValue) {
	if (d.checked){
		$('#inputString').val(" ");
		$.post('get_allcity/');
			
		
	}

}//end of the function
