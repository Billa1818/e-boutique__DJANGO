<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
	
	<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
	<link rel="stylesheet" type="text/css" href="css/head_style.css">
 
	<script class="js/bootstrap.js"></script>
</head>
<body>
  
<header><?php

 

if (isset($_SESSION['user_mail'])) {
  
  $nom=$_SESSION['user_nom'];
}

?>
	
<div class="fixed-top">
  

<nav class="navbar navbar-expand-lg navbar-light bg-light  "
style="background-color: #203543 !important;" 

>
 



  <a class="navbar-brand text-light active " href="#" style="font-weight: bold; font-size: 30px; font-family: cursive; " >E-Boutique</a>
  <button class="navbar-toggler bg-light" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon  "></span>
  </button>

  <div class="collapse navbar-collapse " id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
          
        </a>
      </li><a  href="profil.php"   id="logo1"> <img src="img/user.png" style=" height: 45px ; width: 45px; margin-right: 11px; ">    </a>
       
      <li class="nav-item active">
        
        <a class="nav-link text-light" href="index.php" style="     font-family: cursive; " id="menuH" >Acceuil <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link text-light" href="mes_article.php" style="    font-family: cursive; "  id="menuH">Mes Article</a>
      </li>
       <li class="nav-item">
        <a class="nav-link text-light" href="ajt_article.php" style="    font-family: cursive; "  id="menuH">Ajouter article</a>
      </li>
      <li class="nav-item dropdown " >
        <a class="nav-link dropdown-toggle text-light" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="    font-family: cursive; " >
          Categorie
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">livre</a>
          <a class="dropdown-item" href="#">informatique</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">cosmetique</a>
          <a class="dropdown-item" href="#">...........</a>
          <a class="dropdown-item" href="#">...........</a>
          <a class="dropdown-item" href="#">...........</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link text-light " style="    font-family: cursive; " href="messagerie.php" tabindex="-1"  id="menuH" >Messagerie</a>
      </li>
      <li class="nav-item">
        <a class="nav-link text-light" href="mon_panier.php" style="    font-family: cursive; "  id="menuH">Mon panier</a>
      </li>
      <li class="nav-item">
        <a class="nav-link text-light" href="a_propos.php" style="     font-family: cursive; "  id="menuH"> A propos</a>
      </li>
      <li class="nav-item">
        <a class="nav-link text-light" href="nous_contacter.php" style="    font-family: cursive; "  id="menuH">Nous contacter</a>
      </li>
      
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Rechercher...">
      <button class="btn btn-warning my-2 fw-bold my-sm-0" type="submit">Rechercher</button>
    </form>
  </div>
</nav>

</div>
	
</header>

</body>
</html>