/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package publicarassinar;

import java.util.Arrays;
import java.util.List;

/**
 *
 * @author barbiero
 */
public class PublicarAssinar {

    static final List<Publicante> PUBLISHERS = Arrays.asList(new Publicante("P1"),new Publicante("P2"));
    static final List<Assinante> ASSINANTES = Arrays.asList(new Assinante("A1"), new Assinante("A2"));
    static final List<Intermediario> INTERS = Arrays.asList(
            new Intermediario("I1"),
            new Intermediario("I2"),
            new Intermediario("I3")
    );
    
    static {
        Intermediario i1 = INTERS.get(0);
        Intermediario i2 = INTERS.get(1);
        Intermediario i3 = INTERS.get(2);
        
        i1.addVizinho(i2);
        i1.addVizinho(i3);
        
        i1.addVizinho(PUBLISHERS.get(0));
        
        i2.addVizinho(ASSINANTES.get(0));
        
        i3.addVizinho(PUBLISHERS.get(1));
        i3.addVizinho(ASSINANTES.get(1));
    }
    
    
    static final List<Event> EVENTOS = Arrays.asList(
            new Event("Evento 1"),
            new Event("Evento 2"),
            new Event("Evento 3"),
            new Event("Evento 4"),
            new Event("Evento 5")
    );
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Assinante a1 = ASSINANTES.get(0);
        Assinante a2 = ASSINANTES.get(1);
        
        Event e1 = EVENTOS.get(0);
        Event e2 = EVENTOS.get(1);
        
        a1.assinar(e1);
        a2.assinar(e2);
        
        Publicante p1 = PUBLISHERS.get(0);
        Publicante p2 = PUBLISHERS.get(1);
        
        p1.publishEvent(e2);
        p2.publishEvent(e1);
    }
    
}
