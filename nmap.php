<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="description" content="Liga de basquetbol" />
		<meta name "keywords" content="deporte, Baloncesto" />
		<title>NMAP</title>
		<link rel="stylesheet" type="text/css" href="css.css" />
		
		<script language="JavaScript">
	        function goto(select) { var index=select.selectedIndex
	        if (select.options[index].value != "0") {
	        location=select.options[index].value;}}
	    </script>
	</head>

	<body background="../img/fondo2.jpg"  >

		<div id="agrupar">

			<section id="seccion">
			<?php 
			$base = new PDO ("mysql:host=localhost; dbname=hackiar", "root","");
			$base->setAttribute(PDO::ATTR_ERRMODE , PDO::ERRMODE_EXCEPTION );
			?>

				<article id="articulo">
					<h2 id="mp7">NMAP:</h2>
				</article>
				
				<table id="tabla-cuentas"> 
					<thead id="encabezado-tabla">
					<tr >
						<td>IP</td>
						<td>PUERTO</td>
						<td>SERVICIO</td>
						<td>ESTADO</td>
						<td>FECHA/HORA</td>
									
					</tr>
					</thead>

					<?php 


					$r = $base->prepare("SELECT * FROM  nmap ORDER BY fecha_hora, ip ");

					$r->execute();
					while ($registro = $r->fetch(PDO::FETCH_ASSOC)) {
										
					?>
					<tr>
						<td><?php echo $registro['ip']; ?></td>
						<td><?php echo $registro['puerto']; ?></td>
						<td><?php echo $registro['servicio']; ?></td>
						<td><?php echo $registro['estado']; ?></td>
						<td><?php echo $registro['fecha_hora']; ?></td>
												
					</tr>
					<?php
						} 
					?>
				</table>
			
			</section>
		
		</div>

	</body>
</html>
