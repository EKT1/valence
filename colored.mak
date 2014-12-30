<h5>${_('Emotion detector')} <span style="font-size:80%;color:gray">v0.9</span></h5>
<p>Lõigu vasakus servas on leksikonipõhine hinnang.</p>
<p>
${_('Keywords are')}
<span class="word positiveW">${_('positive')}</span>,
<span class="word negativeW">${_('negative')}</span>
${_('or')}
<span class="word extremeW">${_('extreme')}</span>.
</p>
<p>
${_('Paragraphs are')} 
<span class="para positiveP" style="padding:0px; margin-left:0px">${_('positive')}</span>,
<span class="para negativeP" style="padding:0px; margin-left:0px">${_('negative')}</span>,
<span class="para mixedP" style="padding:0px; margin-left:0px">${_('ambivalent')}</span>,  
<span class="para neutralP" style="padding:0px; margin-left:0px">${_('neutral2')}</span> 
${_('or')}
<span class="para extremeP" style="padding:0px; margin-left:0px">${_('extreme')}</span>.
</p>
<p><i>Lõigu paremas servas on statistiline hinnang.</i></p>

${c.text}
<%def name="styles()">\
<style>
.wide {
        max-width:720px;
}
.text {
  padding-top:2em;
}
.word,.tile {
  border-radius: 5px;
  box-shadow:2px 2px 2px #989898;
}
.positiveW,.positiveT { background-color: rgb(146, 208, 80); }
.negativeW,.negativeT { background-color: #b7a6dd; }
.mixedW,.mixedT       { background-color: #d9ddb4; }
.neutralW,.neutralT   { background-color: white; }
.extremeW,.extremeT       { background-color: darkgray; }

.para {
  padding:1em;
  border-left:5px solid white;
  border-right:5px solid white;
  border-radius: 10px;
  margin-left:10%;
}
.neutralP  { }
.positiveP { border-left-color: rgb(146, 208, 80); }
.negativeP { border-left-color: #b7a6dd; }
.extremeP    { border-left-color: darkgray; }
.mixedP    { border-left-color: #d9ddb4;  border-left-style: dotted; }
.neutralB  { }
.positiveB { border-right-color: rgb(146, 208, 80); }
.negativeB { border-right-color: #b7a6dd; }

div.chart {
  position:relative;
  padding-top:48px;
  margin:0;
  height:48px;
  width:100%;
}
.chart a {
  text-decoration:none;
  color:#555;
}
div.bar {
  /*only needed for height * position:relative;*/
  padding:0px;
  margin:0px;
  height:24px;
  float:left;
  box-shadow:2px 2px 5px #989898;
}
span.info {
  display: none;
  width: 120px;
  position: absolute;
  margin-top: 28px;
  padding:6px 0px 6px 10px;
  font-size:70%;
}
.bar:hover {
  padding: 4px 0 4px 0;
  margin-top: -4px;
}
.bar:hover .info {	
  display: block;
  font-weight: bold; 
  background-color:lightyellow;
  border-radius: 5px;
  box-shadow:2px 2px 5px #989898;
}

</style>
</%def>\
<div class="buttons"><a href="/valence">${_('Back')}</a></div>
<%inherit file="/layout.mak"/>\

