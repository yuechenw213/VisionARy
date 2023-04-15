using System.Collections;
using System.Collections.Generic;

using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(LoadMeshScript))]
public class LoadMeshScriptEditor : Editor
{
    private SerializedProperty fileField;
    private SerializedProperty folderField;

    private void OnEnable()
    {
        fileField = serializedObject.FindProperty("filePath");
        folderField = serializedObject.FindProperty("folderPath");
    }

    public override void OnInspectorGUI()
    {

        serializedObject.Update();

        // Display the fields and buttons in the desired order
        EditorGUILayout.PropertyField(fileField);
        if (GUILayout.Button("Load Mesh"))
        {
            // Load the mesh from the file and set it for the mesh filter component
            ((LoadMeshScript)target).StartLoad();
        }

        EditorGUILayout.PropertyField(folderField);
        if (GUILayout.Button("Load All Mesh"))
        {
            // Load the mesh from the file and set it for the mesh filter component
            ((LoadMeshScript)target).StartLoadFolder();
        }

        serializedObject.ApplyModifiedProperties();

    }
}
