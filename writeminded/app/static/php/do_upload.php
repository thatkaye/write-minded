
    <?php if($_POST['Submit'])
    {
        $upload_path = "files/";
        $target_path = $upload_path . basename($_FILES['myfile']['name']);
        
        if(!file_exists($upload_path))
        {
            echo "unable to laocate folder : <strong>" . $upload_path . "</strong><br>";
            echo "<a href = 'uploadFileIN.html'>Back</a>";
            exit();
        }
        else
        {
            if(@move_uploaded_file($_FILES['myfile']['tmp_nmame'], $target_path))
            {
                echo "file uploaded : <strong>" .$_FILES['myfile']['name']. "</strong>";
                echo "<a href = 'uploadFileIN.html'>Back</a>";
                exit();
            }
        }
    }


