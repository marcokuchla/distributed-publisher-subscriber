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
public class Assinante {

    public Assinante(String name) {
        this.name = name;
    }
    String name;
    
    @Override
    public String toString() {
        return "[" + this.name + "]";
    }
    
    Set<Intermediario> vizinhos = new HashSet<>();

    public Set<Intermediario> getVizinhos() {
        return vizinhos;
    }

    public Set<Event> getAssinaturas() {
        return assinaturas;
    }
    Set<Event> assinaturas = new HashSet<>();
    
    public void assinar(Event event)
    {
        vizinhos.forEach((inter) -> {
           inter.receiveSubscription(event, this);
        });
        
        this.assinaturas.add(event);
    }
    
    public void receiveEvent(Event event)
    {
        System.out.println(this + " recebeu evento " + event.getName());
        if(assinaturas.contains(event)) {
            event.execute();
        }
    }
    
}
