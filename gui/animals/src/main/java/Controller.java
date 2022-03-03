import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import utils.R;

import java.net.URL;
import java.util.ResourceBundle;

public class Controller implements Initializable {

    @FXML
    private ImageView image;
    @FXML
    private Button dog;
    @FXML
    private Button cat;
    @FXML
    private Button llama;
    @FXML
    private Label status;

    @Override
    public void initialize(URL loc, ResourceBundle res) {
        dog.setOnAction((e) -> set("dog"));
        cat.setOnAction((e) -> set("cat"));
        llama.setOnAction((e) -> set("llama"));
    }

    private void set(String name) {
        image.setImage(new Image(R.getResourceAsStream("images/" + name + ".png")));
        status.setText("Showing a " + name);
    }
}
