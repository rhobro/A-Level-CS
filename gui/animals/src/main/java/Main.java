import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;
import utils.R;

public class Main extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage main) throws Exception {
        main.setScene(new Scene(FXMLLoader.load(R.getResource("fxml/main.fxml"))));
        main.setResizable(false);
        main.setTitle("Animals - whyyyyyy");

        main.show();
    }
}
