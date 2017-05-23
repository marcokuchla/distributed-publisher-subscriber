/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package publicarassinar;

import java.util.Collection;
import java.util.EnumSet;

/**
 * Classe de evento a ser publicado
 * @author barbiero
 */
public class Event {

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    
    private String name;
    
    public enum EventTags {
        EVENT_NOTICIA,
        EVENT_PUBLICACAO,
        EVENT_ARTIGO,
        EVENT_AVISO,
        EVENT_END
    };
    
    private final EnumSet<EventTags> tags = EnumSet.noneOf(EventTags.class);

    public EnumSet getTags() {
        return tags;
    }
    
    public boolean hasTag(EventTags tag) {
        return tags.contains(tag);
    }
    
    public boolean hasTags(Collection<EventTags> tag) {
        return tags.containsAll(tag);
    }
    
    public void setTag(EventTags tag) {
        tags.add(tag);
    }
    
    public void setTags(Collection<EventTags> tag) {
        tags.addAll(tag);
    }
    
    public void unsetTag(EventTags tag) {
        tags.remove(tag);
    }
    
    public void unsetTags(Collection<EventTags> tag) {
        tags.removeAll(tag);
    }
    
    void execute() {
        System.out.println("Evento <" + getName() + "> executado.");
    }
    
    Event(String name) {
        this.name = name;
    }
    
    Event(String name, EventTags tag) {
        this.name = name;
        this.tags.add(tag);
    }
    
    Event(String name, Collection<EventTags> tag) {
        this.name = name;
        this.tags.addAll(tag);
    }
    
}
