(function($){
    function CSRFProtection(fn){
        var token=$('meta[name="csrf-token"]').attr('content');
        if(token)fn(function(xhr){
            xhr.setRequestHeader('X-CSRF-Token',token)
            });
    }
    if($().jquery=='1.5'){
        var factory=$.ajaxSettings.xhr;
        $.ajaxSettings.xhr=function(){
            var xhr=factory();
            CSRFProtection(function(setHeader){
                var open=xhr.open;
                xhr.open=function(){
                    open.apply(this,arguments);
                    setHeader(this)
                    };
                
            });
        return xhr;
    };

}
else $(document).ajaxSend(function(e,xhr){
    CSRFProtection(function(setHeader){
        setHeader(xhr)
        });
});
function fire(obj,name,data){
    var event=new $.Event(name);
    obj.trigger(event,data);
    return event.result!==false;
}
function handleRemote(element){
    var method,url,data,dataType=element.attr('data-type')||($.ajaxSettings&&$.ajaxSettings.dataType);
    if(element.is('form')){
        method=element.attr('method');
        url=element.attr('action');
        data=element.serializeArray();
        var button=element.data('ujs:submit-button');
        if(button){
            data.push(button);
            element.data('ujs:submit-button',null);
        }
    }else{
    method=element.attr('data-method');
    url=element.attr('href');
    data=null;
}
$.ajax({
    url:url,
    type:method||'GET',
    data:data,
    dataType:dataType,
    beforeSend:function(xhr,settings){
        if(settings.dataType===undefined){
            xhr.setRequestHeader('accept','*/*;q=0.5, '+settings.accepts.script);
        }
        return fire(element,'ajax:beforeSend',[xhr,settings]);
    },
    success:function(data,status,xhr){
        element.trigger('ajax:success',[data,status,xhr]);
    },
    complete:function(xhr,status){
        element.trigger('ajax:complete',[xhr,status]);
    },
    error:function(xhr,status,error){
        element.trigger('ajax:error',[xhr,status,error]);
    }
});
}
function handleMethod(link){
    var href=link.attr('href'),method=link.attr('data-method'),csrf_token=$('meta[name=csrf-token]').attr('content'),csrf_param=$('meta[name=csrf-param]').attr('content'),form=$('<form method="post" action="'+href+'"></form>'),metadata_input='<input name="_method" value="'+method+'" type="hidden" />';
    if(csrf_param!==undefined&&csrf_token!==undefined){
        metadata_input+='<input name="'+csrf_param+'" value="'+csrf_token+'" type="hidden" />';
    }
    form.hide().append(metadata_input).appendTo('body');
    form.submit();
}
function disableFormElements(form){
    form.find('input[data-disable-with]').each(function(){
        var input=$(this);
        input.data('ujs:enable-with',input.val()).val(input.attr('data-disable-with')).attr('disabled','disabled');
    });
}
function enableFormElements(form){
    form.find('input[data-disable-with]').each(function(){
        var input=$(this);
        input.val(input.data('ujs:enable-with')).removeAttr('disabled');
    });
}
function allowAction(element){
    var message=element.attr('data-confirm');
    return!message||(fire(element,'confirm')&&confirm(message));
}
function requiredValuesMissing(form){
    var missing=false;
    form.find('input[name][required]').each(function(){
        if(!$(this).val())missing=true;
    });
    return missing;
}
$('a[data-confirm], a[data-method], a[data-remote]').live('click.rails',function(e){
    var link=$(this);
    if(!allowAction(link))return false;
    if(link.attr('data-remote')!=undefined){
        handleRemote(link);
        return false;
    }else if(link.attr('data-method')){
        handleMethod(link);
        return false;
    }
});
$('form').live('submit.rails',function(e){
    var form=$(this),remote=form.attr('data-remote')!=undefined;
    if(!allowAction(form))return false;
    if(requiredValuesMissing(form))return!remote;
    if(remote){
        handleRemote(form);
        return false;
    }else{
        setTimeout(function(){
            disableFormElements(form)
            },13);
    }
});
$('form input[type=submit], form button[type=submit], form button:not([type])').live('click.rails',function(){
    var button=$(this);
    if(!allowAction(button))return false;
    var name=button.attr('name'),data=name?{
        name:name,
        value:button.val()
        }:null;
    button.closest('form').data('ujs:submit-button',data);
});
$('form').live('ajax:beforeSend.rails',function(event){
    if(this==event.target)disableFormElements($(this));
});
$('form').live('ajax:complete.rails',function(event){
    if(this==event.target)enableFormElements($(this));
});
})(jQuery);
(function(){
    function g(o){
        console.log("$f.fireEvent",[].slice.call(o))
        }
        function k(q){
        if(!q||typeof q!="object"){
            return q
            }
            var o=new q.constructor();
        for(var p in q){
            if(q.hasOwnProperty(p)){
                o[p]=k(q[p])
                }
            }
        return o
    }
    function m(t,q){
    if(!t){
        return
    }
    var o,p=0,r=t.length;
    if(r===undefined){
        for(o in t){
            if(q.call(t[o],o,t[o])===false){
                break
            }
        }
        }else{
    for(var s=t[0];p<r&&q.call(s,p,s)!==false;s=t[++p]){}
}
return t
}
function c(o){
    return document.getElementById(o)
    }
    function i(q,p,o){
    if(typeof p!="object"){
        return q
        }
        if(q&&p){
        m(p,function(r,s){
            if(!o||typeof s!="function"){
                q[r]=s
                }
            })
    }
    return q
}
function n(s){
    var q=s.indexOf(".");
    if(q!=-1){
        var p=s.slice(0,q)||"*";
        var o=s.slice(q+1,s.length);
        var r=[];
        m(document.getElementsByTagName(p),function(){
            if(this.className&&this.className.indexOf(o)!=-1){
                r.push(this)
                }
            });
    return r
    }
}
function f(o){
    o=o||window.event;
    if(o.preventDefault){
        o.stopPropagation();
        o.preventDefault()
        }else{
        o.returnValue=false;
        o.cancelBubble=true
        }
        return false
    }
    function j(q,o,p){
    q[o]=q[o]||[];
    q[o].push(p)
    }
    function e(){
    return"_"+(""+Math.random()).slice(2,10)
    }
    var h=function(t,r,s){
    var q=this,p={},u={};
    
    q.index=r;
    if(typeof t=="string"){
        t={
            url:t
        }
    }
    i(this,t,true);
m(("Begin*,Start,Pause*,Resume*,Seek*,Stop*,Finish*,LastSecond,Update,BufferFull,BufferEmpty,BufferStop").split(","),function(){
    var v="on"+this;
    if(v.indexOf("*")!=-1){
        v=v.slice(0,v.length-1);
        var w="onBefore"+v.slice(2);
        q[w]=function(x){
            j(u,w,x);
            return q
            }
        }
    q[v]=function(x){
    j(u,v,x);
    return q
    };
    
if(r==-1){
    if(q[w]){
        s[w]=q[w]
        }
        if(q[v]){
        s[v]=q[v]
        }
    }
});
i(this,{
    onCuepoint:function(x,w){
        if(arguments.length==1){
            p.embedded=[null,x];
            return q
            }
            if(typeof x=="number"){
            x=[x]
            }
            var v=e();
        p[v]=[x,w];
        if(s.isLoaded()){
            s._api().fp_addCuepoints(x,r,v)
            }
            return q
        },
    update:function(w){
        i(q,w);
        if(s.isLoaded()){
            s._api().fp_updateClip(w,r)
            }
            var v=s.getConfig();
        var x=(r==-1)?v.clip:v.playlist[r];
        i(x,w,true)
        },
    _fireEvent:function(v,y,w,A){
        if(v=="onLoad"){
            m(p,function(B,C){
                if(C[0]){
                    s._api().fp_addCuepoints(C[0],r,B)
                    }
                });
        return false
        }
        A=A||q;
    if(v=="onCuepoint"){
        var z=p[y];
        if(z){
            return z[1].call(s,A,w)
            }
        }
    if(y&&"onBeforeBegin,onMetaData,onStart,onUpdate,onResume".indexOf(v)!=-1){
    i(A,y);
    if(y.metaData){
        if(!A.duration){
            A.duration=y.metaData.duration
            }else{
            A.fullDuration=y.metaData.duration
            }
        }
}
var x=true;
m(u[v],function(){
    x=this.call(s,A,y,w)
    });
return x
}
});
if(t.onCuepoint){
    var o=t.onCuepoint;
    q.onCuepoint.apply(q,typeof o=="function"?[o]:o);
    delete t.onCuepoint
    }
    m(t,function(v,w){
    if(typeof w=="function"){
        j(u,v,w);
        delete t[v]
    }
});
if(r==-1){
    s.onCuepoint=this.onCuepoint
    }
};

var l=function(p,r,q,t){
    var o=this,s={},u=false;
    if(t){
        i(s,t)
        }
        m(r,function(v,w){
        if(typeof w=="function"){
            s[v]=w;
            delete r[v]
        }
    });
i(this,{
    animate:function(y,z,x){
        if(!y){
            return o
            }
            if(typeof z=="function"){
            x=z;
            z=500
            }
            if(typeof y=="string"){
            var w=y;
            y={};
            
            y[w]=z;
            z=500
            }
            if(x){
            var v=e();
            s[v]=x
            }
            if(z===undefined){
            z=500
            }
            r=q._api().fp_animate(p,y,z,v);
        return o
        },
    css:function(w,x){
        if(x!==undefined){
            var v={};
            
            v[w]=x;
            w=v
            }
            r=q._api().fp_css(p,w);
        i(o,r);
        return o
        },
    show:function(){
        this.display="block";
        q._api().fp_showPlugin(p);
        return o
        },
    hide:function(){
        this.display="none";
        q._api().fp_hidePlugin(p);
        return o
        },
    toggle:function(){
        this.display=q._api().fp_togglePlugin(p);
        return o
        },
    fadeTo:function(y,x,w){
        if(typeof x=="function"){
            w=x;
            x=500
            }
            if(w){
            var v=e();
            s[v]=w
            }
            this.display=q._api().fp_fadeTo(p,y,x,v);
        this.opacity=y;
        return o
        },
    fadeIn:function(w,v){
        return o.fadeTo(1,w,v)
        },
    fadeOut:function(w,v){
        return o.fadeTo(0,w,v)
        },
    getName:function(){
        return p
        },
    getPlayer:function(){
        return q
        },
    _fireEvent:function(w,v,x){
        if(w=="onUpdate"){
            var z=q._api().fp_getPlugin(p);
            if(!z){
                return
            }
            i(o,z);
            delete o.methods;
            if(!u){
                m(z.methods,function(){
                    var B=""+this;
                    o[B]=function(){
                        var C=[].slice.call(arguments);
                        var D=q._api().fp_invoke(p,B,C);
                        return D==="undefined"||D===undefined?o:D
                        }
                    });
            u=true
            }
        }
    var A=s[w];
if(A){
    var y=A.apply(o,v);
    if(w.slice(0,1)=="_"){
        delete s[w]
    }
    return y
    }
    return o
}
})
};

function b(q,G,t){
    var w=this,v=null,D=false,u,s,F=[],y={},x={},E,r,p,C,o,A;
    i(w,{
        id:function(){
            return E
            },
        isLoaded:function(){
            return(v!==null&&v.fp_play!==undefined&&!D)
            },
        getParent:function(){
            return q
            },
        hide:function(H){
            if(H){
                q.style.height="0px"
                }
                if(w.isLoaded()){
                v.style.height="0px"
                }
                return w
            },
        show:function(){
            q.style.height=A+"px";
            if(w.isLoaded()){
                v.style.height=o+"px"
                }
                return w
            },
        isHidden:function(){
            return w.isLoaded()&&parseInt(v.style.height,10)===0
            },
        load:function(J){
            if(!w.isLoaded()&&w._fireEvent("onBeforeLoad")!==false){
                var H=function(){
                    u=q.innerHTML;
                    if(u&&!flashembed.isSupported(G.version)){
                        q.innerHTML=""
                        }
                        if(J){
                        J.cached=true;
                        j(x,"onLoad",J)
                        }
                        flashembed(q,G,{
                        config:t
                    })
                    };
                    
                var I=0;
                m(a,function(){
                    this.unload(function(K){
                        if(++I==a.length){
                            H()
                            }
                        })
                })
            }
            return w
        },
    unload:function(J){
        if(this.isFullscreen()&&/WebKit/i.test(navigator.userAgent)){
            if(J){
                J(false)
                }
                return w
            }
            if(u.replace(/\s/g,"")!==""){
            if(w._fireEvent("onBeforeUnload")===false){
                if(J){
                    J(false)
                    }
                    return w
                }
                D=true;
            try{
                if(v){
                    v.fp_close();
                    w._fireEvent("onUnload")
                    }
                }catch(H){}
        var I=function(){
            v=null;
            q.innerHTML=u;
            D=false;
            if(J){
                J(true)
                }
            };
        
    setTimeout(I,50)
        }else{
        if(J){
            J(false)
            }
        }
    return w
},
getClip:function(H){
    if(H===undefined){
        H=C
        }
        return F[H]
    },
getCommonClip:function(){
    return s
    },
getPlaylist:function(){
    return F
    },
getPlugin:function(H){
    var J=y[H];
    if(!J&&w.isLoaded()){
        var I=w._api().fp_getPlugin(H);
        if(I){
            J=new l(H,I,w);
            y[H]=J
            }
        }
    return J
},
getScreen:function(){
    return w.getPlugin("screen")
    },
getControls:function(){
    return w.getPlugin("controls")._fireEvent("onUpdate")
    },
getLogo:function(){
    try{
        return w.getPlugin("logo")._fireEvent("onUpdate")
        }catch(H){}
},
getPlay:function(){
    return w.getPlugin("play")._fireEvent("onUpdate")
    },
getConfig:function(H){
    return H?k(t):t
    },
getFlashParams:function(){
    return G
    },
loadPlugin:function(K,J,M,L){
    if(typeof M=="function"){
        L=M;
        M={}
    }
    var I=L?e():"_";
w._api().fp_loadPlugin(K,J,M,I);
var H={};

H[I]=L;
var N=new l(K,null,w,H);
y[K]=N;
return N
},
getState:function(){
    return w.isLoaded()?v.fp_getState():-1
    },
play:function(I,H){
    var J=function(){
        if(I!==undefined){
            w._api().fp_play(I,H)
            }else{
            w._api().fp_play()
            }
        };
    
if(w.isLoaded()){
    J()
    }else{
    if(D){
        setTimeout(function(){
            w.play(I,H)
            },50)
        }else{
        w.load(function(){
            J()
            })
        }
    }
return w
},
getVersion:function(){
    var I="flowplayer.js 3.2.6";
    if(w.isLoaded()){
        var H=v.fp_getVersion();
        H.push(I);
        return H
        }
        return I
    },
_api:function(){
    if(!w.isLoaded()){
        throw"Flowplayer "+w.id()+" not loaded when calling an API method"
        }
        return v
    },
setClip:function(H){
    w.setPlaylist([H]);
    return w
    },
getIndex:function(){
    return p
    },
_swfHeight:function(){
    return v.clientHeight
    }
});
m(("Click*,Load*,Unload*,Keypress*,Volume*,Mute*,Unmute*,PlaylistReplace,ClipAdd,Fullscreen*,FullscreenExit,Error,MouseOver,MouseOut").split(","),function(){
    var H="on"+this;
    if(H.indexOf("*")!=-1){
        H=H.slice(0,H.length-1);
        var I="onBefore"+H.slice(2);
        w[I]=function(J){
            j(x,I,J);
            return w
            }
        }
    w[H]=function(J){
    j(x,H,J);
    return w
    }
});
m(("pause,resume,mute,unmute,stop,toggle,seek,getStatus,getVolume,setVolume,getTime,isPaused,isPlaying,startBuffering,stopBuffering,isFullscreen,toggleFullscreen,reset,close,setPlaylist,addClip,playFeed,setKeyboardShortcutsEnabled,isKeyboardShortcutsEnabled").split(","),function(){
    var H=this;
    w[H]=function(J,I){
        if(!w.isLoaded()){
            return w
            }
            var K=null;
        if(J!==undefined&&I!==undefined){
            K=v["fp_"+H](J,I)
            }else{
            K=(J===undefined)?v["fp_"+H]():v["fp_"+H](J)
            }
            return K==="undefined"||K===undefined?w:K
        }
    });
w._fireEvent=function(Q){
    if(typeof Q=="string"){
        Q=[Q]
        }
        var R=Q[0],O=Q[1],M=Q[2],L=Q[3],K=0;
    if(t.debug){
        g(Q)
        }
        if(!w.isLoaded()&&R=="onLoad"&&O=="player"){
        v=v||c(r);
        o=w._swfHeight();
        m(F,function(){
            this._fireEvent("onLoad")
            });
        m(y,function(S,T){
            T._fireEvent("onUpdate")
            });
        s._fireEvent("onLoad")
        }
        if(R=="onLoad"&&O!="player"){
        return
    }
    if(R=="onError"){
        if(typeof O=="string"||(typeof O=="number"&&typeof M=="number")){
            O=M;
            M=L
            }
        }
    if(R=="onContextMenu"){
    m(t.contextMenu[O],function(S,T){
        T.call(w)
        });
    return
}
if(R=="onPluginEvent"||R=="onBeforePluginEvent"){
    var H=O.name||O;
    var I=y[H];
    if(I){
        I._fireEvent("onUpdate",O);
        return I._fireEvent(M,Q.slice(3))
        }
        return
}
if(R=="onPlaylistReplace"){
    F=[];
    var N=0;
    m(O,function(){
        F.push(new h(this,N++,w))
        })
    }
    if(R=="onClipAdd"){
    if(O.isInStream){
        return
    }
    O=new h(O,M,w);
    F.splice(M,0,O);
    for(K=M+1;K<F.length;K++){
        F[K].index++
    }
    }
    var P=true;
if(typeof O=="number"&&O<F.length){
    C=O;
    var J=F[O];
    if(J){
        P=J._fireEvent(R,M,L)
        }
        if(!J||P!==false){
        P=s._fireEvent(R,M,L,J)
        }
    }
m(x[R],function(){
    P=this.call(w,O,M);
    if(this.cached){
        x[R].splice(K,1)
        }
        if(P===false){
        return false
        }
        K++
});
return P
};

function B(){
    if($f(q)){
        $f(q).getParent().innerHTML="";
        p=$f(q).getIndex();
        a[p]=w
        }else{
        a.push(w);
        p=a.length-1
        }
        A=parseInt(q.style.height,10)||q.clientHeight;
    E=q.id||"fp"+e();
    r=G.id||E+"_api";
    G.id=r;
    t.playerId=E;
    if(typeof t=="string"){
        t={
            clip:{
                url:t
            }
        }
    }
if(typeof t.clip=="string"){
    t.clip={
        url:t.clip
        }
    }
t.clip=t.clip||{};

if(q.getAttribute("href",2)&&!t.clip.url){
    t.clip.url=q.getAttribute("href",2)
    }
    s=new h(t.clip,-1,w);
t.playlist=t.playlist||[t.clip];
var I=0;
m(t.playlist,function(){
    var K=this;
    if(typeof K=="object"&&K.length){
        K={
            url:""+K
            }
        }
    m(t.clip,function(L,M){
    if(M!==undefined&&K[L]===undefined&&typeof M!="function"){
        K[L]=M
        }
    });
t.playlist[I]=K;
K=new h(K,I,w);
F.push(K);
I++
});
m(t,function(K,L){
    if(typeof L=="function"){
        if(s[K]){
            s[K](L)
            }else{
            j(x,K,L)
            }
            delete t[K]
    }
});
m(t.plugins,function(K,L){
    if(L){
        y[K]=new l(K,L,w)
        }
    });
if(!t.plugins||t.plugins.controls===undefined){
    y.controls=new l("controls",null,w)
    }
    y.canvas=new l("canvas",null,w);
u=q.innerHTML;
function J(L){
    var K=w.hasiPadSupport&&w.hasiPadSupport();
    if(/iPad|iPhone|iPod/i.test(navigator.userAgent)&&!/.flv$/i.test(F[0].url)&&!K){
        return true
        }
        if(!w.isLoaded()&&w._fireEvent("onBeforeClick")!==false){
        w.load()
        }
        return f(L)
    }
    function H(){
    if(u.replace(/\s/g,"")!==""){
        if(q.addEventListener){
            q.addEventListener("click",J,false)
            }else{
            if(q.attachEvent){
                q.attachEvent("onclick",J)
                }
            }
    }else{
    if(q.addEventListener){
        q.addEventListener("click",f,false)
        }
        w.load()
    }
}
setTimeout(H,0)
}
if(typeof q=="string"){
    var z=c(q);
    if(!z){
        throw"Flowplayer cannot access element: "+q
        }
        q=z;
    B()
    }else{
    B()
    }
}
var a=[];
function d(o){
    this.length=o.length;
    this.each=function(p){
        m(o,p)
        };
        
    this.size=function(){
        return o.length
        }
    }
window.flowplayer=window.$f=function(){
    var p=null;
    var o=arguments[0];
    if(!arguments.length){
        m(a,function(){
            if(this.isLoaded()){
                p=this;
                return false
                }
            });
    return p||a[0]
    }
    if(arguments.length==1){
    if(typeof o=="number"){
        return a[o]
        }else{
        if(o=="*"){
            return new d(a)
            }
            m(a,function(){
            if(this.id()==o.id||this.id()==o||this.getParent()==o){
                p=this;
                return false
                }
            });
    return p
    }
}
if(arguments.length>1){
    var t=arguments[1],q=(arguments.length==3)?arguments[2]:{};
    
    if(typeof t=="string"){
        t={
            src:t
        }
    }
    t=i({
    bgcolor:"#000000",
    version:[9,0],
    expressInstall:"http://static.flowplayer.org/swf/expressinstall.swf",
    cachebusting:false
},t);
if(typeof o=="string"){
    if(o.indexOf(".")!=-1){
        var s=[];
        m(n(o),function(){
            s.push(new b(this,k(t),k(q)))
            });
        return new d(s)
        }else{
        var r=c(o);
        return new b(r!==null?r:o,t,q)
        }
    }else{
    if(o){
        return new b(o,t,q)
        }
    }
}
return null
};

i(window.$f,{
    fireEvent:function(){
        var o=[].slice.call(arguments);
        var q=$f(o[0]);
        return q?q._fireEvent(o.slice(1)):null
        },
    addPlugin:function(o,p){
        b.prototype[o]=p;
        return $f
        },
    each:m,
    extend:i
});
if(typeof jQuery=="function"){
    jQuery.fn.flowplayer=function(q,p){
        if(!arguments.length||typeof arguments[0]=="number"){
            var o=[];
            this.each(function(){
                var r=$f(this);
                if(r){
                    o.push(r)
                    }
                });
        return arguments.length?o[arguments[0]]:new d(o)
        }
        return this.each(function(){
        $f(this,k(q),p?k(p):{})
        })
    }
}
})();
(function(){
    var e=typeof jQuery=="function";
    var i={
        width:"100%",
        height:"100%",
        allowfullscreen:true,
        allowscriptaccess:"always",
        quality:"high",
        version:null,
        onFail:null,
        expressInstall:null,
        w3c:false,
        cachebusting:false
    };
    
    if(e){
        jQuery.tools=jQuery.tools||{};
        
        jQuery.tools.flashembed={
            version:"1.0.4",
            conf:i
        }
    }
    function j(){
    if(c.done){
        return false
        }
        var l=document;
    if(l&&l.getElementsByTagName&&l.getElementById&&l.body){
        clearInterval(c.timer);
        c.timer=null;
        for(var k=0;k<c.ready.length;k++){
            c.ready[k].call()
            }
            c.ready=null;
        c.done=true
        }
    }
var c=e?jQuery:function(k){
    if(c.done){
        return k()
        }
        if(c.timer){
        c.ready.push(k)
        }else{
        c.ready=[k];
        c.timer=setInterval(j,13)
        }
    };

function f(l,k){
    if(k){
        for(key in k){
            if(k.hasOwnProperty(key)){
                l[key]=k[key]
                }
            }
        }
        return l
}
function g(k){
    switch(h(k)){
        case"string":
            k=k.replace(new RegExp('(["\\\\])',"g"),"\\$1");
            k=k.replace(/^\s?(\d+)%/,"$1pct");
            return'"'+k+'"';
        case"array":
            return"["+b(k,function(n){
            return g(n)
            }).join(",")+"]";
        case"function":
            return'"function()"';
        case"object":
            var l=[];
            for(var m in k){
            if(k.hasOwnProperty(m)){
                l.push('"'+m+'":'+g(k[m]))
                }
            }
        return"{"+l.join(",")+"}"
        }
        return String(k).replace(/\s/g," ").replace(/\'/g,'"')
}
function h(l){
    if(l===null||l===undefined){
        return false
        }
        var k=typeof l;
    return(k=="object"&&l.push)?"array":k
    }
    if(window.attachEvent){
    window.attachEvent("onbeforeunload",function(){
        __flash_unloadHandler=function(){};
        
        __flash_savedUnloadHandler=function(){}
    })
}
function b(k,n){
    var m=[];
    for(var l in k){
        if(k.hasOwnProperty(l)){
            m[l]=n(k[l])
            }
        }
    return m
}
function a(r,t){
    var q=f({},r);
    var s=document.all;
    var n='<object width="'+q.width+'" height="'+q.height+'"';
    if(s&&!q.id){
        q.id="_"+(""+Math.random()).substring(9)
        }
        if(q.id){
        n+=' id="'+q.id+'"'
        }
        if(q.cachebusting){
        q.src+=((q.src.indexOf("?")!=-1?"&":"?")+Math.random())
        }
        if(q.w3c||!s){
        n+=' data="'+q.src+'" type="application/x-shockwave-flash"'
        }else{
        n+=' classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"'
        }
        n+=">";
    if(q.w3c||s){
        n+='<param name="movie" value="'+q.src+'" />'
        }
        q.width=q.height=q.id=q.w3c=q.src=null;
    for(var l in q){
        if(q[l]!==null){
            n+='<param name="'+l+'" value="'+q[l]+'" />'
            }
        }
    var o="";
if(t){
    for(var m in t){
        if(t[m]!==null){
            o+=m+"="+(typeof t[m]=="object"?g(t[m]):t[m])+"&"
            }
        }
    o=o.substring(0,o.length-1);
n+='<param name="flashvars" value=\''+o+"' />"
}
n+="</object>";
return n
}
function d(m,p,l){
    var k=flashembed.getVersion();
    f(this,{
        getContainer:function(){
            return m
            },
        getConf:function(){
            return p
            },
        getVersion:function(){
            return k
            },
        getFlashvars:function(){
            return l
            },
        getApi:function(){
            return m.firstChild
            },
        getHTML:function(){
            return a(p,l)
            }
        });
var q=p.version;
var r=p.expressInstall;
var o=!q||flashembed.isSupported(q);
if(o){
    p.onFail=p.version=p.expressInstall=null;
    m.innerHTML=a(p,l)
    }else{
    if(q&&r&&flashembed.isSupported([6,65])){
        f(p,{
            src:r
        });
        l={
            MMredirectURL:location.href,
            MMplayerType:"PlugIn",
            MMdoctitle:document.title
            };
            
        m.innerHTML=a(p,l)
        }else{
        if(m.innerHTML.replace(/\s/g,"")!==""){}else{
            m.innerHTML="<h2>Flash version "+q+" or greater is required</h2><h3>"+(k[0]>0?"Your version is "+k:"You have no flash plugin installed")+"</h3>"+(m.tagName=="A"?"<p>Click here to download latest version</p>":"<p>Download latest version from <a href='http://www.adobe.com/go/getflashplayer'>here</a></p>");
            if(m.tagName=="A"){
                m.onclick=function(){
                    location.href="http://www.adobe.com/go/getflashplayer"
                    }
                }
        }
}
}
if(!o&&p.onFail){
    var n=p.onFail.call(this);
    if(typeof n=="string"){
        m.innerHTML=n
        }
    }
if(document.all){
    window[p.id]=document.getElementById(p.id)
    }
}
window.flashembed=function(l,m,k){
    if(typeof l=="string"){
        var n=document.getElementById(l);
        if(n){
            l=n
            }else{
            c(function(){
                flashembed(l,m,k)
                });
            return
        }
    }
    if(!l){
    return
}
if(typeof m=="string"){
    m={
        src:m
    }
}
var o=f({},i);
f(o,m);
return new d(l,o,k)
};

f(window.flashembed,{
    getVersion:function(){
        var m=[0,0];
        if(navigator.plugins&&typeof navigator.plugins["Shockwave Flash"]=="object"){
            var l=navigator.plugins["Shockwave Flash"].description;
            if(typeof l!="undefined"){
                l=l.replace(/^.*\s+(\S+\s+\S+$)/,"$1");
                var n=parseInt(l.replace(/^(.*)\..*$/,"$1"),10);
                var r=/r/.test(l)?parseInt(l.replace(/^.*r(.*)$/,"$1"),10):0;
                m=[n,r]
                }
            }else{
        if(window.ActiveXObject){
            try{
                var p=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.7")
                }catch(q){
                try{
                    p=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.6");
                    m=[6,0];
                    p.AllowScriptAccess="always"
                    }catch(k){
                    if(m[0]==6){
                        return m
                        }
                    }
                try{
                p=new ActiveXObject("ShockwaveFlash.ShockwaveFlash")
                }catch(o){}
        }
        if(typeof p=="object"){
        l=p.GetVariable("$version");
        if(typeof l!="undefined"){
            l=l.replace(/^\S+\s+(.*)$/,"$1").split(",");
            m=[parseInt(l[0],10),parseInt(l[2],10)]
            }
        }
}
}
return m
},
isSupported:function(k){
    var m=flashembed.getVersion();
    var l=(m[0]>k[0])||(m[0]==k[0]&&m[1]>=k[1]);
    return l
    },
domReady:c,
asString:g,
getHTML:a
});
if(e){
    jQuery.fn.flashembed=function(l,k){
        var m=null;
        this.each(function(){
            m=flashembed(this,l,k)
            });
        return l.api===false?this:m
        }
    }
})();
(function($){
    $.extend({
        metadata:{
            defaults:{
                type:'class',
                name:'metadata',
                cre:/({.*})/,
                single:'metadata'
            },
            setType:function(type,name){
                this.defaults.type=type;
                this.defaults.name=name;
            },
            get:function(elem,opts){
                var settings=$.extend({},this.defaults,opts);
                if(!settings.single.length)settings.single='metadata';
                var data=$.data(elem,settings.single);
                if(data)return data;
                data="{}";
                if(settings.type=="class"){
                    var m=settings.cre.exec(elem.className);
                    if(m)
                        data=m[1];
                }else if(settings.type=="elem"){
                    if(!elem.getElementsByTagName)return;
                    var e=elem.getElementsByTagName(settings.name);
                    if(e.length)
                        data=$.trim(e[0].innerHTML);
                }else if(elem.getAttribute!=undefined){
                    var attr=elem.getAttribute(settings.name);
                    if(attr)
                        data=attr;
                }
                if(data.indexOf('{')<0)
                    data="{"+data+"}";
                data=eval("("+data+")");
                $.data(elem,settings.single,data);
                return data;
            }
        }
    });
$.fn.metadata=function(opts){
    return $.metadata.get(this[0],opts);
};

})(jQuery);
eval(function(p,a,c,k,e,r){
    e=function(c){
        return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))
        };
        
    if(!''.replace(/^/,String)){
        while(c--)r[e(c)]=k[c]||e(c);
        k=[function(e){
            return r[e]
            }];
        e=function(){
            return'\\w+'
            };
            
        c=1
        };
    while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);
    return p
    }(';5(29.1j)(7($){5($.1L.1J)1I{1t.1H("1K",J,H)}1M(e){};$.n.3=7(i){5(4.Q==0)k 4;5(A I[0]==\'1h\'){5(4.Q>1){8 j=I;k 4.W(7(){$.n.3.y($(4),j)})};$.n.3[I[0]].y(4,$.1T(I).1U(1)||[]);k 4};8 i=$.12({},$.n.3.1s,i||{});$.n.3.K++;4.2a(\'.9-3-1f\').o(\'9-3-1f\').W(7(){8 a,l=$(4);8 b=(4.23||\'21-3\').1v(/\\[|\\]/g,\'Z\').1v(/^\\Z+|\\Z+$/g,\'\');8 c=$(4.1X||1t.1W);8 d=c.6(\'3\');5(!d||d.18!=$.n.3.K)d={z:0,18:$.n.3.K};8 e=d[b];5(e)a=e.6(\'3\');5(e&&a)a.z++;x{a=$.12({},i||{},($.1b?l.1b():($.1S?l.6():s))||{},{z:0,F:[],v:[]});a.w=d.z++;e=$(\'<1R V="9-3-1Q"/>\');l.1P(e);e.o(\'3-15-T-17\');5(l.S(\'R\'))a.m=H;e.1c(a.E=$(\'<P V="3-E"><a 14="\'+a.E+\'">\'+a.1d+\'</a></P>\').1g(7(){$(4).3(\'O\');$(4).o(\'9-3-N\')}).1i(7(){$(4).3(\'u\');$(4).G(\'9-3-N\')}).1l(7(){$(4).3(\'r\')}).6(\'3\',a))};8 f=$(\'<P V="9-3 q-\'+a.w+\'"><a 14="\'+(4.14||4.1p)+\'">\'+4.1p+\'</a></P>\');e.1c(f);5(4.11)f.S(\'11\',4.11);5(4.1r)f.o(4.1r);5(a.1F)a.t=2;5(A a.t==\'1u\'&&a.t>0){8 g=($.n.10?f.10():0)||a.1w;8 h=(a.z%a.t),Y=1y.1z(g/a.t);f.10(Y).1A(\'a\').1B({\'1C-1D\':\'-\'+(h*Y)+\'1E\'})};5(a.m)f.o(\'9-3-1o\');x f.o(\'9-3-1G\').1g(7(){$(4).3(\'1n\');$(4).3(\'D\')}).1i(7(){$(4).3(\'u\');$(4).3(\'C\')}).1l(7(){$(4).3(\'r\')});5(4.L)a.p=f;l.1q();l.1N(7(){$(4).3(\'r\')});f.6(\'3.l\',l.6(\'3.9\',f));a.F[a.F.Q]=f[0];a.v[a.v.Q]=l[0];a.q=d[b]=e;a.1O=c;l.6(\'3\',a);e.6(\'3\',a);f.6(\'3\',a);c.6(\'3\',d)});$(\'.3-15-T-17\').3(\'u\').G(\'3-15-T-17\');k 4};$.12($.n.3,{K:0,D:7(){8 a=4.6(\'3\');5(!a)k 4;5(!a.D)k 4;8 b=$(4).6(\'3.l\')||$(4.U==\'13\'?4:s);5(a.D)a.D.y(b[0],[b.M(),$(\'a\',b.6(\'3.9\'))[0]])},C:7(){8 a=4.6(\'3\');5(!a)k 4;5(!a.C)k 4;8 b=$(4).6(\'3.l\')||$(4.U==\'13\'?4:s);5(a.C)a.C.y(b[0],[b.M(),$(\'a\',b.6(\'3.9\'))[0]])},1n:7(){8 a=4.6(\'3\');5(!a)k 4;5(a.m)k;4.3(\'O\');4.1a().19().X(\'.q-\'+a.w).o(\'9-3-N\')},O:7(){8 a=4.6(\'3\');5(!a)k 4;5(a.m)k;a.q.1V().X(\'.q-\'+a.w).G(\'9-3-1k\').G(\'9-3-N\')},u:7(){8 a=4.6(\'3\');5(!a)k 4;4.3(\'O\');5(a.p){a.p.6(\'3.l\').S(\'L\',\'L\');a.p.1a().19().X(\'.q-\'+a.w).o(\'9-3-1k\')}x $(a.v).1m(\'L\');a.E[a.m||a.1Y?\'1q\':\'1Z\']();4.20()[a.m?\'o\':\'G\'](\'9-3-1o\')},r:7(a,b){8 c=4.6(\'3\');5(!c)k 4;5(c.m)k;c.p=s;5(A a!=\'B\'){5(A a==\'1u\')k $(c.F[a]).3(\'r\',B,b);5(A a==\'1h\')$.W(c.F,7(){5($(4).6(\'3.l\').M()==a)$(4).3(\'r\',B,b)})}x c.p=4[0].U==\'13\'?4.6(\'3.9\'):(4.22(\'.q-\'+c.w)?4:s);4.6(\'3\',c);4.3(\'u\');8 d=$(c.p?c.p.6(\'3.l\'):s);5((b||b==B)&&c.1e)c.1e.y(d[0],[d.M(),$(\'a\',c.p)[0]])},m:7(a,b){8 c=4.6(\'3\');5(!c)k 4;c.m=a||a==B?H:J;5(b)$(c.v).S("R","R");x $(c.v).1m("R");4.6(\'3\',c);4.3(\'u\')},1x:7(){4.3(\'m\',H,H)},24:7(){4.3(\'m\',J,J)}});$.n.3.1s={E:\'25 26\',1d:\'\',t:0,1w:16};$(7(){$(\'l[27=28].9\').3()})})(1j);',62,135,'|||rating|this|if|data|function|var|star|||||||||||return|input|readOnly|fn|addClass|current|rater|select|null|split|draw|inputs|serial|else|apply|count|typeof|undefined|blur|focus|cancel|stars|removeClass|true|arguments|false|calls|checked|val|hover|drain|div|length|disabled|attr|be|tagName|class|each|filter|spw|_|width|id|extend|INPUT|title|to||drawn|call|andSelf|prevAll|metadata|append|cancelValue|callback|applied|mouseover|string|mouseout|jQuery|on|click|removeAttr|fill|readonly|value|hide|className|options|document|number|replace|starWidth|disable|Math|floor|find|css|margin|left|px|half|live|execCommand|try|msie|BackgroundImageCache|browser|catch|change|context|before|control|span|meta|makeArray|slice|children|body|form|required|show|siblings|unnamed|is|name|enable|Cancel|Rating|type|radio|window|not'.split('|'),0,{}));

(function($){
    var ie6=$.browser.msie&&parseInt($.browser.version)===6&&typeof window['XMLHttpRequest']!=='object',ie7=$.browser.msie&&parseInt($.browser.version)===7,ieQuirks=null,w=[];
    $.modal=function(data,options){
        return $.modal.impl.init(data,options);
    };
    
    $.modal.close=function(){
        $.modal.impl.close();
    };
    
    $.modal.focus=function(pos){
        $.modal.impl.focus(pos);
    };
    
    $.modal.setContainerDimensions=function(){
        $.modal.impl.setContainerDimensions();
    };
    
    $.modal.setPosition=function(){
        $.modal.impl.setPosition();
    };
    
    $.modal.update=function(height,width){
        $.modal.impl.update(height,width);
    };
    
    $.fn.modal=function(options){
        return $.modal.impl.init(this,options);
    };
    
    $.modal.defaults={
        appendTo:'body',
        focus:true,
        opacity:50,
        overlayId:'simplemodal-overlay',
        overlayCss:{},
        containerId:'simplemodal-container',
        containerCss:{},
        dataId:'simplemodal-data',
        dataCss:{},
        minHeight:null,
        minWidth:null,
        maxHeight:null,
        maxWidth:null,
        autoResize:false,
        autoPosition:true,
        zIndex:1000,
        close:true,
        closeHTML:'<a class="modalCloseImg" title="Close"></a>',
        closeClass:'simplemodal-close',
        escClose:true,
        overlayClose:false,
        position:null,
        persist:false,
        modal:true,
        onOpen:null,
        onShow:null,
        onClose:null
    };
    
    $.modal.impl={
        d:{},
        init:function(data,options){
            var s=this;
            if(s.d.data){
                return false;
            }
            ieQuirks=$.browser.msie&&!$.boxModel;
            s.o=$.extend({},$.modal.defaults,options);
            s.zIndex=s.o.zIndex;
            s.occb=false;
            if(typeof data==='object'){
                data=data instanceof jQuery?data:$(data);
                s.d.placeholder=false;
                if(data.parent().parent().size()>0){
                    data.before($('<span></span>').attr('id','simplemodal-placeholder').css({
                        display:'none'
                    }));
                    s.d.placeholder=true;
                    s.display=data.css('display');
                    if(!s.o.persist){
                        s.d.orig=data.clone(true);
                    }
                }
            }
    else if(typeof data==='string'||typeof data==='number'){
        data=$('<div></div>').html(data);
    }
    else{
        alert('SimpleModal Error: Unsupported data type: '+typeof data);
        return s;
    }
    s.create(data);
    data=null;
    s.open();
    if($.isFunction(s.o.onShow)){
        s.o.onShow.apply(s,[s.d]);
    }
    return s;
},
create:function(data){
    var s=this;
    w=s.getDimensions();
    if(s.o.modal&&ie6){
        s.d.iframe=$('<iframe src="javascript:false;"></iframe>').css($.extend(s.o.iframeCss,{
            display:'none',
            opacity:0,
            position:'fixed',
            height:w[0],
            width:w[1],
            zIndex:s.o.zIndex,
            top:0,
            left:0
        })).appendTo(s.o.appendTo);
    }
    s.d.overlay=$('<div></div>').attr('id',s.o.overlayId).addClass('simplemodal-overlay').css($.extend(s.o.overlayCss,{
        display:'none',
        opacity:s.o.opacity/100,
        height:s.o.modal?w[0]:0,
        width:s.o.modal?w[1]:0,
        position:'fixed',
        left:0,
        top:0,
        zIndex:s.o.zIndex+1
        })).appendTo(s.o.appendTo);
    s.d.container=$('<div></div>').attr('id',s.o.containerId).addClass('simplemodal-container').css($.extend(s.o.containerCss,{
        display:'none',
        position:'fixed',
        zIndex:s.o.zIndex+2
        })).append(s.o.close&&s.o.closeHTML?$(s.o.closeHTML).addClass(s.o.closeClass):'').appendTo(s.o.appendTo);
    s.d.wrap=$('<div></div>').attr('tabIndex',-1).addClass('simplemodal-wrap').css({
        height:'100%',
        outline:0,
        width:'100%'
    }).appendTo(s.d.container);
    s.d.data=data.attr('id',data.attr('id')||s.o.dataId).addClass('simplemodal-data').css($.extend(s.o.dataCss,{
        display:'none'
    })).appendTo('body');
    data=null;
    s.setContainerDimensions();
    s.d.data.appendTo(s.d.wrap);
    if(ie6||ieQuirks){
        s.fixIE();
    }
},
bindEvents:function(){
    var s=this;
    $('.'+s.o.closeClass).bind('click.simplemodal',function(e){
        e.preventDefault();
        s.close();
    });
    if(s.o.modal&&s.o.close&&s.o.overlayClose){
        s.d.overlay.bind('click.simplemodal',function(e){
            e.preventDefault();
            s.close();
        });
    }
    $(document).bind('keydown.simplemodal',function(e){
        if(s.o.modal&&e.keyCode===9){
            s.watchTab(e);
        }
        else if((s.o.close&&s.o.escClose)&&e.keyCode===27){
            e.preventDefault();
            s.close();
        }
    });
$(window).bind('resize.simplemodal',function(){
    w=s.getDimensions();
    s.o.autoResize?s.setContainerDimensions():s.o.autoPosition&&s.setPosition();
    if(ie6||ieQuirks){
        s.fixIE();
    }
    else if(s.o.modal){
        s.d.iframe&&s.d.iframe.css({
            height:w[0],
            width:w[1]
            });
        s.d.overlay.css({
            height:w[0],
            width:w[1]
            });
    }
});
},
unbindEvents:function(){
    $('.'+this.o.closeClass).unbind('click.simplemodal');
    $(document).unbind('keydown.simplemodal');
    $(window).unbind('resize.simplemodal');
    this.d.overlay.unbind('click.simplemodal');
},
fixIE:function(){
    var s=this,p=s.o.position;
    $.each([s.d.iframe||null,!s.o.modal?null:s.d.overlay,s.d.container],function(i,el){
        if(el){
            var bch='document.body.clientHeight',bcw='document.body.clientWidth',bsh='document.body.scrollHeight',bsl='document.body.scrollLeft',bst='document.body.scrollTop',bsw='document.body.scrollWidth',ch='document.documentElement.clientHeight',cw='document.documentElement.clientWidth',sl='document.documentElement.scrollLeft',st='document.documentElement.scrollTop',s=el[0].style;
            s.position='absolute';
            if(i<2){
                s.removeExpression('height');
                s.removeExpression('width');
                s.setExpression('height',''+bsh+' > '+bch+' ? '+bsh+' : '+bch+' + "px"');
                s.setExpression('width',''+bsw+' > '+bcw+' ? '+bsw+' : '+bcw+' + "px"');
            }
            else{
                var te,le;
                if(p&&p.constructor===Array){
                    var top=p[0]?typeof p[0]==='number'?p[0].toString():p[0].replace(/px/,''):el.css('top').replace(/px/,'');
                    te=top.indexOf('%')===-1?top+' + (t = '+st+' ? '+st+' : '+bst+') + "px"':parseInt(top.replace(/%/,''))+' * (('+ch+' || '+bch+') / 100) + (t = '+st+' ? '+st+' : '+bst+') + "px"';
                    if(p[1]){
                        var left=typeof p[1]==='number'?p[1].toString():p[1].replace(/px/,'');
                        le=left.indexOf('%')===-1?left+' + (t = '+sl+' ? '+sl+' : '+bsl+') + "px"':parseInt(left.replace(/%/,''))+' * (('+cw+' || '+bcw+') / 100) + (t = '+sl+' ? '+sl+' : '+bsl+') + "px"';
                    }
                }
            else{
                te='('+ch+' || '+bch+') / 2 - (this.offsetHeight / 2) + (t = '+st+' ? '+st+' : '+bst+') + "px"';
                le='('+cw+' || '+bcw+') / 2 - (this.offsetWidth / 2) + (t = '+sl+' ? '+sl+' : '+bsl+') + "px"';
            }
            s.removeExpression('top');
            s.removeExpression('left');
            s.setExpression('top',te);
            s.setExpression('left',le);
        }
    }
    });
},
focus:function(pos){
    var s=this,p=pos&&$.inArray(pos,['first','last'])!==-1?pos:'first';
    var input=$(':input:enabled:visible:'+p,s.d.wrap);
    setTimeout(function(){
        input.length>0?input.focus():s.d.wrap.focus();
    },10);
},
getDimensions:function(){
    var el=$(window);
    var h=$.browser.opera&&$.browser.version>'9.5'&&$.fn.jquery<'1.3'||$.browser.opera&&$.browser.version<'9.5'&&$.fn.jquery>'1.2.6'?el[0].innerHeight:el.height();
    return[h,el.width()];
},
getVal:function(v,d){
    return v?(typeof v==='number'?v:v==='auto'?0:v.indexOf('%')>0?((parseInt(v.replace(/%/,''))/100)*(d==='h'?w[0]:w[1])):parseInt(v.replace(/px/,''))):null;
},
update:function(height,width){
    var s=this;
    if(!s.d.data){
        return false;
    }
    s.d.origHeight=s.getVal(height,'h');
    s.d.origWidth=s.getVal(width,'w');
    s.d.data.hide();
    height&&s.d.container.css('height',height);
    width&&s.d.container.css('width',width);
    s.setContainerDimensions();
    s.d.data.show();
    s.o.focus&&s.focus();
    s.unbindEvents();
    s.bindEvents();
},
setContainerDimensions:function(){
    var s=this,badIE=ie6||ie7;
    var ch=s.d.origHeight?s.d.origHeight:$.browser.opera?s.d.container.height():s.getVal(badIE?s.d.container[0].currentStyle['height']:s.d.container.css('height'),'h'),cw=s.d.origWidth?s.d.origWidth:$.browser.opera?s.d.container.width():s.getVal(badIE?s.d.container[0].currentStyle['width']:s.d.container.css('width'),'w'),dh=s.d.data.outerHeight(true),dw=s.d.data.outerWidth(true);
    s.d.origHeight=s.d.origHeight||ch;
    s.d.origWidth=s.d.origWidth||cw;
    var mxoh=s.o.maxHeight?s.getVal(s.o.maxHeight,'h'):null,mxow=s.o.maxWidth?s.getVal(s.o.maxWidth,'w'):null,mh=mxoh&&mxoh<w[0]?mxoh:w[0],mw=mxow&&mxow<w[1]?mxow:w[1];
    var moh=s.o.minHeight?s.getVal(s.o.minHeight,'h'):'auto';
    if(!ch){
        if(!dh){
            ch=moh;
        }
        else{
            if(dh>mh){
                ch=mh;
            }
            else if(s.o.minHeight&&moh!=='auto'&&dh<moh){
                ch=moh;
            }
            else{
                ch=dh;
            }
        }
    }
else{
    ch=s.o.autoResize&&ch>mh?mh:ch<moh?moh:ch;
}
var mow=s.o.minWidth?s.getVal(s.o.minWidth,'w'):'auto';
if(!cw){
    if(!dw){
        cw=mow;
    }
    else{
        if(dw>mw){
            cw=mw;
        }
        else if(s.o.minWidth&&mow!=='auto'&&dw<mow){
            cw=mow;
        }
        else{
            cw=dw;
        }
    }
}
else{
    cw=s.o.autoResize&&cw>mw?mw:cw<mow?mow:cw;
}
s.d.container.css({
    height:ch,
    width:cw
});
s.d.wrap.css({
    overflow:(dh>ch||dw>cw)?'auto':'visible'
    });
s.o.autoPosition&&s.setPosition();
},
setPosition:function(){
    var s=this,top,left,hc=(w[0]/2)-(s.d.container.outerHeight(true)/2),vc=(w[1]/2)-(s.d.container.outerWidth(true)/2);
    if(s.o.position&&Object.prototype.toString.call(s.o.position)==='[object Array]'){
        top=s.o.position[0]||hc;
        left=s.o.position[1]||vc;
    }else{
        top=hc;
        left=vc;
    }
    s.d.container.css({
        left:left,
        top:top
    });
},
watchTab:function(e){
    var s=this;
    if($(e.target).parents('.simplemodal-container').length>0){
        s.inputs=$(':input:enabled:visible:first, :input:enabled:visible:last',s.d.data[0]);
        if((!e.shiftKey&&e.target===s.inputs[s.inputs.length-1])||(e.shiftKey&&e.target===s.inputs[0])||s.inputs.length===0){
            e.preventDefault();
            var pos=e.shiftKey?'last':'first';
            s.focus(pos);
        }
    }
else{
    e.preventDefault();
    s.focus();
}
},
open:function(){
    var s=this;
    s.d.iframe&&s.d.iframe.show();
    if($.isFunction(s.o.onOpen)){
        s.o.onOpen.apply(s,[s.d]);
    }
    else{
        s.d.overlay.show();
        s.d.container.show();
        s.d.data.show();
    }
    s.o.focus&&s.focus();
    s.bindEvents();
},
close:function(){
    var s=this;
    if(!s.d.data){
        return false;
    }
    s.unbindEvents();
    if($.isFunction(s.o.onClose)&&!s.occb){
        s.occb=true;
        s.o.onClose.apply(s,[s.d]);
    }
    else{
        if(s.d.placeholder){
            var ph=$('#simplemodal-placeholder');
            if(s.o.persist){
                ph.replaceWith(s.d.data.removeClass('simplemodal-data').css('display',s.display));
            }
            else{
                s.d.data.hide().remove();
                ph.replaceWith(s.d.orig);
            }
        }
    else{
        s.d.data.hide().remove();
    }
    s.d.container.hide().remove();
    s.d.overlay.hide();
    s.d.iframe&&s.d.iframe.hide().remove();
    setTimeout(function(){
        s.d.overlay.remove();
        s.d={};
    
    },10);
}
}
};

})(jQuery);
(function($){
    $.fn.extend({
        limit:function(limit,element){
            var interval,f;
            var self=$(this);
            $(this).focus(function(){
                interval=window.setInterval(substring,100);
            });
            $(this).blur(function(){
                clearInterval(interval);
                substring();
            });
            if(typeof $(self).val()!='undefined')

            {
                substringFunction="function substring(){ var val = $(self).val();var length = val.length;if(length > limit){$(self).val($(self).val().substring(0,limit));}";
                if(typeof element!='undefined')
                    substringFunction+="if($(element).html() != limit-length){$(element).html((limit-length<=0)?'0':limit-length);}"
                substringFunction+="}";
                eval(substringFunction);
                substring();
            }
        }
    });
})(jQuery);
(function($){
    $.placeholderLabel={
        placeholder_class:null,
        add_placeholder:function(){
            if($(this).val()==$(this).attr('placeholder')){
                $(this).val('').removeClass($.placeholderLabel.placeholder_class);
            }
        },
    remove_placeholder:function(){
        if($(this).val()==''){
            $(this).val($(this).attr('placeholder')).addClass($.placeholderLabel.placeholder_class);
        }
    },
disable_placeholder_fields:function(){
    $(this).find("input[placeholder]").each(function(){
        if($(this).val()==$(this).attr('placeholder')){
            $(this).val('');
        }
    });
return true;
}
};

$.fn.placeholderLabel=function(options){
    var dummy=document.createElement('input');
    if(dummy.placeholder!=undefined){
        return this;
    }
    var config={
        placeholder_class:'placeholder'
    };
    
    if(options)$.extend(config,options);
    $.placeholderLabel.placeholder_class=config.placeholder_class;
    this.each(function(){
        var input=$(this);
        input.focus($.placeholderLabel.add_placeholder);
        input.blur($.placeholderLabel.remove_placeholder);
        input.triggerHandler('focus');
        input.triggerHandler('blur');
        $(this.form).submit($.placeholderLabel.disable_placeholder_fields);
    });
    return this;
}
})(jQuery);
$(document).ready(function($){
    $("#reviews").tabs({
        spinner:'<img src="/images/spinner.gif"/>'
    });
    $('.star').rating({
        readOnly:false,
        required:true
    });
    $('input:text[placeholder]').placeholderLabel();
    $("#q").autocomplete({
        source:'/autocomplete',
        minLength:3,
        close: function( event, ui ) {
            $('#search_muvi').submit();
        }
    });
    $("#pagination a").live("click",function(){
        $.getScript(this.href);
        return false;
    });
    $("#coming_soon_sort").live("change",function(){
        $.get('/coming_soon_movies','sort='+$('#coming_soon_sort').val(),null,"script");
        return false;
    });
    $('#review_description').limit('250','#reviewCharsLeft');
    $(".items").sortable();
    $("#movies  input[id^=item_]").autocomplete({
        source:'/moviedropdown?type=movies',
        minLength:2,
        select: function( event, ui ) {
        	if(ui.item.poster_file_name != null){
                  $("#"+"img_"+$(this).attr("id") + "> img").attr( "src", "/system/posters/"+ui.item.poster_id+"/thumb/"+ ui.item.poster_file_name);
                }
                else if(ui.item.picture != null){
        		$("#"+"img_"+$(this).attr("id") + "> img").attr( "src", "/system/posters/"+ui.item.id+"/thumb/"+ ui.item.picture);
        	}
        	$("#"+"id_"+$(this).attr("id")).val( ui.item.id);
        }
    }).focus(function(){ $(this).parent().parent().next().show()});
    $("#celebs  input[id^=item_]").autocomplete({
        source:'/moviedropdown?type=celebs',
        minLength:2,
        select: function( event, ui ) {
                if(ui.item.poster_file_name != null){
                  $("#"+"img_"+$(this).attr("id") + "> img").attr( "src", "/system/posters/"+ui.item.poster_id+"/thumb/"+ ui.item.poster_file_name);
                }
                else if(ui.item.picture != null){
                       $("#"+"img_"+$(this).attr("id") + "> img").attr( "src", "/system/profile_pictures/"+ui.item.id+"/thumb/"+ ui.item.picture);
                }
                $("#"+"id_"+$(this).attr("id")).val( ui.item.id);
        }
    }).focus(function(){ $(this).parent().parent().next().show()});
});
function removeMe(item){
if(item != 1){
  $("#item_"+item).val('');
  $("#id_item_"+item).val(0);
  $("#note_"+item).val('');
  $("#img_item_"+item + "> img").attr("src", "/images/no-image.png");
  $("#item_"+item).parent().parent().hide();
}
}

function critics_reviews_sort(movie_id,value){
    var url='/critics_reviews?id='+movie_id+'&sort='+value;
    $.getScript(url);
    return false;
}
function go_to_tab(index){
    $("#reviews").tabs("select",index);
    window.location.hash='#reviews';
}
function popupCenter(url,width,height,name){
    var left=(screen.width/2)-(width/2);
    var top=(screen.height/2)-(height/2);
    return window.open(url,name,"menubar=no,toolbar=no,status=no,width="+width+",height="+height+",toolbar=no,left="+left+",top="+top);
}
function registration(){
    $('#registration').html('');
    $('#registration').modal({
        minHeight:360,
        minWidth:555,
        containerId:'register_from',
        onShow: function(model){
            //for(var i=0; i<5; i++)
            var t=setTimeout("$.modal.setContainerDimensions()", 1000);
        }
    });
    //$.modal.setContainerDimensions();
    var t=setTimeout("enableLoginErrorHide();", 5000);
    return false;
}
function login(){
    /*$('#registration').html('');
    $('#registration').modal({
        minHeight:434,
        minWidth:631,
        containerId:'login_from'
    });
    return false;*/
    registration();
    //enableLoginErrorHide();
}
$(document).ready(function($){
    $("a.popup").click(function(e){
        popupCenter($(this).attr("href"),$(this).attr("data-width"),$(this).attr("data-height"),"authPopup");
        e.stopPropagation();
        return false;
    });
});
$(document).ready(function(){
    $('.trailerLink').click(function(event){
        event.preventDefault();
        $('#trailer').modal({
            minHeight:330,
            minWidth:520,
            containerId:'videoPlayer'
        });
        $f().play();
        return false;
    });
    $('.MovieTrailerLink').click(function(event){
        event.preventDefault();
        movie_id=this.id.split('movie_link_')[1];

        flowplayer("movie_video_"+movie_id, "/flash/flowplayer.commercial-3.2.7.swf", { key: '#$8fe04ea70c52430ec72',logo: {url: '/images/flowplayerLogo.png',fullscreenOnly: false, top: 278, right: 2, opacity: 0.5  },clip: {autoPlay: false, autoBuffering: false  }  });

        $("#movie_"+movie_id).modal({
            minHeight:330,
            minWidth:520,
            containerId:'videoPlayer'
        });
        var player_id="movie_video_"+movie_id;
        $f(player_id).play();
        return false;
    });
  
    $('.remote_trailerLink').click(function(event){
        event.preventDefault();
        $('#trailer').modal({
            minHeight:330,
            minWidth:560,
            containerId:'videoPlayer'
        });
        $("#player").show();
        return false;
    });

    $('.remote_MovieTrailerLink').click(function(event){
        event.preventDefault();
        movie_id=this.id.split('movie_link_')[1];
        $("#movie_"+movie_id).modal({
            minHeight:330,
            minWidth:560,
            containerId:'videoPlayer'
        });
        var player_id="movie_video_"+movie_id;
        $("#player_"+movie_id).show();
        return false;
    });

    $('.MovieTrailerLink_1').click(function(event){
        event.preventDefault();
        movie_id=this.id.split('movie_link_')[1];

        flowplayer("movie_video_"+movie_id, "/flash/flowplayer.commercial-3.2.7.swf", { key: '#$8fe04ea70c52430ec72',logo: {url: '/images/flowplayerLogo.png',fullscreenOnly: false, top: 278, right: 2, opacity: 0.5  },clip: {autoPlay: false, autoBuffering: false  }  });

        $("#movie_"+movie_id).modal({
            minHeight:330,
            minWidth:520,
            containerId:'videoPlayer'
        });
        var player_id="movie_video_"+movie_id;
        $f(player_id).play();
        return false;
    });


});
function validate_blank(search_box){
    if($.trim($("#"+search_box).val()) == ""){
        return false;
    }else{
        return true;
    }
}

