components {
  id: "luma"
  component: "/main/luma.script"
}
embedded_components {
  id: "sprite"
  type: "sprite"
  data: "default_animation: \"luma\"\n"
  "material: \"/builtins/materials/sprite.material\"\n"
  "textures {\n"
  "  sampler: \"texture_sampler\"\n"
  "  texture: \"/atlases/game.atlas\"\n"
  "}\n"
  ""
}
