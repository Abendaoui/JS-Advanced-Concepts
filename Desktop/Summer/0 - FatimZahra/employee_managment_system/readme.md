use the composer dep
use Cocur\Slugify\Slugify;

$slugify = new Slugify();
$slug = $slugify->slugify('Hello World'); // Output: hello-world


Js Bootstrap Files
<!-- Add Bootstrap CSS -->
<link href="node_modules/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Add Bootstrap JavaScript (popper.js is a dependency for some Bootstrap components) -->
<script src="node_modules/popper.js/dist/umd/popper.min.js"></script>
<script src="node_modules/bootstrap/dist/js/bootstrap.min.js"></script>
