package jupiterpi.biomevision.crawler;

import org.bukkit.Bukkit;
import org.bukkit.ChatColor;
import org.bukkit.entity.Player;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Date;

public class Crawler {
    private Player player;

    public Crawler(Player player) {
        this.player = player;
    }

    public void start() {
        player.sendMessage(ChatColor.GREEN + "Starting crawling!");
    }

    public void step() {
        Bukkit.getServer().getConsoleSender().sendMessage("step");
        player.sendMessage("Step.");

        try {
            Robot robot = new Robot();
            Toolkit toolkit = Toolkit.getDefaultToolkit();
            Dimension screenSize = toolkit.getScreenSize();
            Image image = robot.createScreenCapture(new Rectangle(0, 0, screenSize.width, screenSize.height));

            BufferedImage bufferedImage = new BufferedImage(image.getWidth(null), image.getHeight(null), BufferedImage.TYPE_INT_ARGB);
            Graphics2D bGr = bufferedImage.createGraphics();
            bGr.drawImage(image, 0, 0, null);
            bGr.dispose();
            File file = new File("screenshot_" + new Date().getTime() + ".png");
            ImageIO.write(bufferedImage, "png", file);

            // https://stackoverflow.com/questions/13605248/java-converting-image-to-bufferedimage
            // https://stackoverflow.com/questions/464593/how-to-capture-selected-screen-of-other-application-using-java
        } catch (AWTException | IOException e) {
            e.printStackTrace();
        }
    }

    public void stop() {
        player.sendMessage(ChatColor.RED + "Stopped crawling!");
    }
}