

<div class="sidebar left">
	<div class="GrayHeaderBox">
		<div class="sidebar_header">
			<h3>Top 10 Upcomming </h3>
			
		</div>
		<?php
			foreach($top10UC as $uc){
				if($uc[0]->id){
					?>
					
					<div class="row" style="height: 60px;">
						<div class="image">
							<a href="<?php echo site_url('getmovie/index/'.$uc[0]->id); ?>">
								<img src="<?php echo $uc[0]->image; ?>">
							</a>
						</div>
						<div class="left" style="margin-top: -40px; margin-left: 47px;">
							<label>Name  :</label><?php echo $uc[0]->name; ?><br>
							<label>Rating:</label><?php echo $uc[0]->rating; ?><br>
							<label>Runtime:</label><?php if($uc[0]->runtime) {echo$uc[0]->runtime ;} ?><br>
							
						</div>
					</div>
				<?}
			}
			?>
	</div>
	<div class="GrayHeaderBox">
		<div class="sidebar_header">
			<h3>Top 10 Opeinging </h3>
		</div>
		<?php
			foreach($top10OP as $uc){
				if($uc[0]->id)
				{
					?>
					<div class="row">
						<div class="image">
							<a href="<?php echo site_url('getmovie/index/'.$uc[0]->id); ?>">
								<img src="<?php echo $uc[0]->image; ?>">
							</a>
						</div>
						<div class="left" style="margin-top: -40px; margin-left: 47px;">
							<label>Name  :</label><?php echo $uc[0]->name; ?><br>
							<label>Rating:</label><?php echo $uc[0]->rating; ?><br>
							<label>Runtime:</label><?php if($uc[0]->runtime) {echo$uc[0]->runtime ;} ?><br>
							
						</div>
					</div>
			  <?}
			}
			?>
	</div>
</div>
<div class="container left" style="width: 610px; min-height:700px; margin-top: 6px;">
	<h2> <?php echo $title; ?></h2>
	
	<div class="clear"></div>
	<div id="msg_slideshow" class="msg_slideshow">
		<div id="msg_wrapper" class="msg_wrapper">
		</div>
		<div id="msg_controls" class="msg_controls"><!-- right has to animate to 15px, default -110px -->
			
			<a href="#" id="msg_prev" class="msg_prev"></a>
			<a href="#" id="msg_pause_play" class="msg_pause"></a><!-- has to change to msg_play if paused-->
			<a href="#" id="msg_next" class="msg_next"></a>
		</div>
		<div id="msg_thumbs" class="msg_thumbs"><!-- top has to animate to 0px, default -230px -->
				<div class="msg_thumb_wrapper">
					<a href="#"><img src="images/1.jpg" alt="images/1.jpg"/></a>
					<a href="#"><img src="images/2.jpg" alt="images/2.jpg"/></a>
					<a href="#"><img src="images/3.jpg" alt="images/3.jpg"/></a>
					<a href="#"><img src="images/4.jpg" alt="images/4.jpg"/></a>
					<a href="#"><img src="images/5.jpg" alt="images/5.jpg"/></a>
					<a href="#"><img src="images/6.jpg" alt="images/6.jpg"/></a>
				</div>
				
			<a href="#" id="msg_thumb_next" class="msg_thumb_next"></a>
			<a href="#" id="msg_thumb_prev" class="msg_thumb_prev"></a>
			<a href="#" id="msg_thumb_close" class="msg_thumb_close"></a>
			<span class="msg_loading"></span><!-- show when next thumb wrapper loading -->
		</div>
	</div>
	<div class="clear"></div>
	<h1>Our Database Statistics</h1>
	<p> We have total <?php echo $st['movie'] ;?> Movies in our database </p>
	<p> We have total <?php echo $st['actor'] ;?> stars in our database </p>
	<p> We have total <?php echo $st['director'] ;?> director in our database </p>
	<p> We have total <?php echo $st['writer'] ;?> writer in our database </p>
	<p> We have total <?php echo $st['cast'] ;?> cast in our database </p>
	<p> We have total <?php echo $st['image'] ;?> image in our database </p>
	<div class="clear"></div>"
</div>
<div class="sidebar right">
	<div class="GrayHeaderBox">
		<div class="sidebar_header">
			<h3>Top 10 Boxoffice </h3>
		</div>
		<?php
			foreach($top10BF as $uc){
				if($uc[0]->id)
				{
					?>
					<div class="row">
						<div class="image">
							<a href="<?php echo site_url('getmovie/index/'.$uc[0]->id); ?>">
								<img src="<?php echo $uc[0]->image; ?>">
							</a>
						</div>
						<div class="left" style="margin-top: -40px; margin-left: 47px;">
							<label>Name  :</label><?php echo $uc[0]->name; ?><br>
							<label>Rating:</label><?php echo $uc[0]->rating; ?><br>
							<label>Runtime:</label><?php if($uc[0]->runtime) {echo$uc[0]->runtime ;} ?><br>
							
						</div>
					</div>
					<?
				}
			}
			?>
	</div>
	<div class="GrayHeaderBox">
		<div class="sidebar_header">
			<h3>Top 10 Theater </h3>
		</div>
		<?php
			foreach($top10TR as $uc){
				if($uc[0]->id)
				{
					?>
					<div class="row">
						<div class="image">
							<a href="<?php echo site_url('getmovie/index/'.$uc[0]->id); ?>">
								<img src="<?php echo $uc[0]->image; ?>">
							</a>
						</div>
						<div class="left" style="margin-top: -40px; margin-left: 47px;">
							<label>Name  :</label><?php echo $uc[0]->name; ?><br>
							<label>Rating:</label><?php echo $uc[0]->rating; ?><br>
							<label>Runtime:</label><?php if($uc[0]->budget) {echo$uc[0]->runtime ;} ?><br>
							
						</div>
					</div>
					<?
				}
			}
			?>
	</div>
</div>
