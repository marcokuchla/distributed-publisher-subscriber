/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package publicarassinar;

import java.util.HashSet;
import java.util.Set;

/**
 *
 * @author barbiero
 */
public class Publicante {
    
    String name;

    public Publicante(String name) {
        this.name = name;
    }
    
    @Override
    public String toString(){
        return "[" + this.name + "]";
    };
    
    Set<Intermediario> vizinhos = new HashSet<>();

    public Set<Intermediario> getVizinhos() {
        return vizinhos;
    }
    public void publishEvent(Event event) {
        System.out.println(this + " publicando: " + event.getName());
        
        vizinhos.forEach((inter) -> {
            inter.receivePublish(event, null);
        });
    }
    
}
