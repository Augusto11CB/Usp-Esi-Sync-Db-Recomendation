package com.erudia.demo.resource;

import com.FiltroAndReco.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.AutoConfigurationPackage;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;



@RestController
@RequestMapping("/filtros") // "/buscar"
public class FiltroResource{

    //@Autowired
    //private Filtro f;
    private Buscar b;
    private IndexMannager mIndex = new IndexMannager(7000, 101);

//    @PostMapping
//http://localhost:8080/filtros/coisa
    @GetMapping("/{buscar}/{pesquisa}")
    public String buscar(@PathVariable String buscar, @PathVariable String[] pesquisa){
        // String[] ids = pesquisa.split(",");
        b = new Buscar();
        try{
            Thread.sleep(5000);

        } catch(Exception e){
            e.printStackTrace();
        }
        String superPesquisa = "";
        for (String p : pesquisa){
            superPesquisa = superPesquisa + p;
        }
        return buscar + superPesquisa;
    }

    @GetMapping("/papagaio/{fala}")
    public String papagaioFala(@PathVariable String fala){
        return fala;
    }

    @GetMapping("/papagaio2/{fala}")
    public String papagaioFala2(@PathVariable String fala){
        String resp = JythonComunication.SendToPython(mIndex, fala);
        return resp;
    }
    
    
    

}