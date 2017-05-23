/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package publicarassinar;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 *
 * @author barbiero
 */
public class Intermediario {
    //List<Intermediario> routing;
    //List<Assinante> assinaturas;
    
    private final Map<Event, Set<Intermediario> > routing = new HashMap<>();
    private final Map<Event, Set<Assinante> > assinaturas = new HashMap<>();
    
    private final Set<Intermediario> vizinhos = new HashSet<>();
    
    public void addVizinho(Intermediario inter) {
        this.vizinhos.add(inter);
        inter.vizinhos.add(this);
    }
    
    public void addVizinho(Assinante assinante) {
        assinante.vizinhos.add(this);
    }
    
    public void addVizinho(Publicante publ) {
        publ.vizinhos.add(this);
    }
    
    public Set<Intermediario> getVizinhos() {
        return this.vizinhos;
    }
    
    
    
    public void receiveSubscription(Event event, Assinante assinante)
    {
        Set<Assinante> assinantes = this.assinaturas.get(event);
        if(assinantes == null) {
            assinantes = new HashSet<>();
            this.assinaturas.put(event, assinantes);
        }
        
        assinantes.add(assinante);
        
        this.vizinhos.forEach((inter) -> {
            inter.receiveSubscriptionNotice(event, this);
        });
    }
    
    public void receiveSubscriptionNotice(Event event, Intermediario source)
    {
        Set<Intermediario> rota = routing.get(event);
        if(rota == null) {
            rota = new HashSet<>();
            routing.put(event, rota);
        }
        
        rota.add(source);
        
        this.vizinhos.stream().filter(i->i!=source).forEach(i->{
            i.receiveSubscriptionNotice(event, this);
        });
    }
    
    
    public void receivePublish(Event event, Intermediario source) {
        
        System.out.println(this + " recebeu evento " + event.getName() + " de " + source);
        
        Set<Assinante> matchList = assinaturas.get(event);
        if(matchList != null) {
            matchList.forEach((a)->a.receiveEvent(event));
        }
        
        Set<Intermediario> fwList = routing.get(event);
        if(fwList != null) {
            fwList.stream().filter(i -> i != source).forEach(i->{
                i.receivePublish(event, this);
            });
        }
    }

    public Intermediario(String name) {
        this.name = name;
    }
    
    String name;

    @Override
    public String toString() {
        return "{" + name + '}';
    }
    
    
    
}
